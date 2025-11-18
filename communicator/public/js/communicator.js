(() => {
  const refresh_channels = async (wrapper) => {
    const channel_area = wrapper.querySelector('[data-role="channel-list"]');
    channel_area.innerHTML = '<div class="communicator__placeholder">Loading channels...</div>';

    const { message } = await frappe.call({
      method: 'frappe.client.get_list',
      args: {
        doctype: 'Communicator Channel',
        fields: ['name', 'title', 'is_private'],
        order_by: 'modified desc',
        limit_page_length: 50,
      },
    });

    channel_area.innerHTML = '';
    if (!message || !message.length) {
      channel_area.innerHTML = '<div class="communicator__placeholder">No channels yet.</div>';
      return;
    }

    message.forEach((channel) => {
      const row = document.createElement('button');
      row.type = 'button';
      row.className = 'communicator__channel';
      row.dataset.channel = channel.name;
      row.innerHTML = `
        <div class="communicator__channel-title">${frappe.utils.escape_html(channel.title || channel.name)}</div>
        <div class="communicator__channel-meta">${channel.is_private ? 'Private' : 'Open'}</div>
      `;
      row.addEventListener('click', () => refresh_messages(wrapper, channel.name));
      channel_area.appendChild(row);
    });
  };

  const refresh_messages = async (wrapper, channel_name) => {
    const message_area = wrapper.querySelector('[data-role="message-list"]');
    message_area.innerHTML = '<div class="communicator__placeholder">Loading messages...</div>';

    const { message } = await frappe.call({
      method: 'frappe.client.get_list',
      args: {
        doctype: 'Communicator Message',
        fields: ['name', 'body', 'owner', 'creation'],
        filters: { channel: channel_name },
        order_by: 'creation desc',
        limit_page_length: 100,
      },
    });

    message_area.innerHTML = '';
    if (!message || !message.length) {
      message_area.innerHTML = '<div class="communicator__placeholder">No messages yet.</div>';
      return;
    }

    message.reverse().forEach((doc) => {
      const row = document.createElement('div');
      row.className = 'communicator__message';
      row.innerHTML = `
        <div class="communicator__message-body">${frappe.utils.escape_html(doc.body || '')}</div>
        <div class="communicator__message-meta">${frappe.utils.escape_html(doc.owner || '')} · ${frappe.datetime.user_to_str(doc.creation)}</div>
      `;
      message_area.appendChild(row);
    });

    const input = wrapper.querySelector('[data-role="composer"]');
    input.dataset.channel = channel_name;
    input.disabled = false;
    input.placeholder = 'Type a message and press Enter';
    input.focus();
  };

  const send_message = async (wrapper, channel_name, body) => {
    const message_area = wrapper.querySelector('[data-role="message-list"]');
    message_area.insertAdjacentHTML(
      'beforeend',
      `<div class="communicator__message communicator__message--pending"><div class="communicator__message-body">${frappe.utils.escape_html(body)}</div><div class="communicator__message-meta">Sending…</div></div>`
    );

    try {
      await frappe.call({
        method: 'frappe.client.insert',
        args: {
          doc: {
            doctype: 'Communicator Message',
            channel: channel_name,
            body,
          },
        },
      });
      await refresh_messages(wrapper, channel_name);
    } catch (error) {
      frappe.msgprint({
        title: 'Could not send message',
        indicator: 'red',
        message: error.message || error,
      });
      await refresh_messages(wrapper, channel_name);
    }
  };

  frappe.pages['communicator-messenger'] = {
    on_page_load(wrapper) {
      wrapper.classList.add('communicator__page');
      wrapper.innerHTML = `
        <div class="communicator__panel communicator__panel--left">
          <div class="communicator__panel-header">Channels</div>
          <div class="communicator__scroll" data-role="channel-list"></div>
        </div>
        <div class="communicator__panel communicator__panel--right">
          <div class="communicator__panel-header">Conversation</div>
          <div class="communicator__scroll" data-role="message-list"></div>
          <input class="communicator__composer" data-role="composer" type="text" placeholder="Select a channel to start" disabled />
        </div>
      `;

      const composer = wrapper.querySelector('[data-role="composer"]');
      composer.addEventListener('keydown', async (ev) => {
        if (ev.key !== 'Enter' || !composer.dataset.channel || !composer.value.trim()) return;
        const body = composer.value.trim();
        composer.value = '';
        composer.disabled = true;
        await send_message(wrapper, composer.dataset.channel, body);
      });

      refresh_channels(wrapper);
    },
  };
})();

frappe.pages["curriculum-hub"].on_page_load = function (wrapper) {
  const page = frappe.ui.make_app_page({
    parent: wrapper,
    title: __("Curriculum Hub"),
    single_column: true,
  });

  $(page.body).html(`
    <div class="cc-hub">
      <div class="cc-header">
        <div>
          <div class="cc-title">${__("Curriculum Intelligence")}</div>
          <div class="cc-subtitle">${__("Collate frameworks, plan delivery, and monitor grading.")}</div>
        </div>
      </div>
      <div class="cc-metric-grid"></div>
    </div>
  `);

  frappe.call({
    method: "curriculum_collation.api.curriculum_overview",
    callback: function (r) {
      curriculum_collation.render_metric_cards(page.body, r.message || {});
    },
  });
};

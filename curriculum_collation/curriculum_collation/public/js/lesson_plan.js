frappe.ui.form.on("Lesson Plan", {
  refresh(frm) {
    if (frm.doc.docstatus === 0) {
      frm.dashboard.add_comment(
        "info",
        __("Use Markdown notes to keep instructional delivery concise and reusable.")
      );
    }
  },
});

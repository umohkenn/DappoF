frappe.ui.form.on("Homework Submission", {
  validate(frm) {
    if (frm.doc.score && frm.doc.max_score && frm.doc.score > frm.doc.max_score) {
      frappe.throw(__("Score cannot exceed max score."));
    }
  },
});

frappe.ui.form.on("Curriculum Transition Plan", {
	refresh(frm) {
		frm.set_query("course", () => ({
			filters: frm.doc.program ? { program: frm.doc.program } : {}
		}));

		frm.set_query("unit", () => ({
			filters: frm.doc.course ? { name: ["like", `${frm.doc.course}%`] } : {}
		}));
	}
});

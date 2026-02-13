frappe.listview_settings["Curriculum Transition Plan"] = {
	add_fields: ["status", "course", "curriculum_map", "curriculum_completion_percent"],
	get_indicator(doc) {
		const colors = {
			Draft: "grey",
			"In Progress": "blue",
			Review: "orange",
			Completed: "green",
			Archived: "darkgrey"
		};
		return [__(doc.status), colors[doc.status] || "grey", "status,=," + doc.status];
	}
};

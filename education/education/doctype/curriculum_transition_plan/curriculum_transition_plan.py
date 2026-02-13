# Copyright (c) 2026
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CurriculumTransitionPlan(Document):
	def validate(self):
		self._validate_dates()
		self._validate_completion()

	def _validate_dates(self):
		if self.planned_start_date and self.planned_end_date and self.planned_start_date > self.planned_end_date:
			frappe.throw("Planned Start Date cannot be after Planned End Date")

		if self.actual_start_date and self.actual_end_date and self.actual_start_date > self.actual_end_date:
			frappe.throw("Actual Start Date cannot be after Actual End Date")

	def _validate_completion(self):
		for value, label in [
			(self.curriculum_completion_percent, "Curriculum Completion %"),
			(self.standards_completion_percent, "Standards Completion %"),
		]:
			if value is not None and (value < 0 or value > 100):
				frappe.throw(f"{label} must be between 0 and 100")

frappe.provide("curriculum_collation");

curriculum_collation.render_metric_cards = function (wrapper, stats) {
  const cards = [
    { label: "Frameworks", key: "framework_count", icon: "education" },
    { label: "Active Courses", key: "active_courses", icon: "book" },
    { label: "Weekly Schemes", key: "weekly_schemes", icon: "calendar" },
    { label: "Pending Grading", key: "pending_grading", icon: "edit" },
  ];

  const html = cards
    .map(
      (card) => `
      <div class="cc-card">
        <div class="cc-card__label">${card.label}</div>
        <div class="cc-card__value">${stats[card.key] || 0}</div>
      </div>
    `
    )
    .join("");

  $(wrapper).find(".cc-metric-grid").html(html);
};

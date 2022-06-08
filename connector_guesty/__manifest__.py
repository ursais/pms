{
    "name": "PMS Guesty Connector",
    "author": "Casai, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/pms",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": [
        "pms_base",
        "pms_sale",
        "queue_job",
        "sale_automatic_workflow",
        "payment",
        "pms_website",
        "crm",
        "product",
        "base_automation",
    ],
    "data": [
        "views/backend_guesty.xml",
        "views/pms_property.xml",
        "views/pms_property_reservation.xml",
        "views/pms_reservation.xml",
        "views/pms_website_views.xml",
        "views/pms_guesty_calendar.xml",
        "views/pms_guesty_calendar_wizard.xml",
        "views/res_partner.xml",
        "views/sale_order_views.xml",
        "views/sale_order_report_custom.xml",
        "views/sales_order_portal_template_custom.xml",
        "views/product_template_views.xml",
        "wizard/pms_property_days_quotation_expiration_views.xml",
        "wizard/crm_lead_new_reservation.xml",
        "views/property_assets.xml",
        "views/pms_property_picture.xml",
        "security/ir.model.access.csv",
        "data/queue.job.function.csv",
        "data/ir_cron.xml",
        "data/base_automation.xml",
        "templates/header_01.xml",
        "templates/dynamic_amenities.xml",
        "templates/info_bar_01.xml",
        "templates/section_about_apt.xml",
        "templates/fixed_amenities.xml",
        "templates/section_dynamic_reviews.xml",
        "templates/section_location.xml",
        "templates/section_policies.xml",
    ],
    "installable": True,
    "development_status": "Beta",
    "maintainers": ["JorgeJuarezCasai"],
    "external_dependencies": {"python": ["html2text"]},
}

# Copyright 2018 Surekha Technologies (https://www.surekhatech.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Website OCA Integrator",
    "summary": "Displays Integrators in website.",
    "version": "13.0.1.0.0",
    "category": "Website",
    "license": "AGPL-3",
    "website": "https://github.com/OCA/oca-custom",
    "author": "Odoo Community Association (OCA), Surekha Technologies",
    "depends": [
        "base",
        "website",
        "website_crm_partner_assign",
        "website_sale",
        "membership",
        "website_membership",
        "website_customer",
        "apps_product_creator",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/assets.xml",
        "views/website_oca_integrator_templates.xml",
        "views/website_oca_integrator_product_templates.xml",
        "views/website_oca_integrator_contributor_templates.xml",
        "views/view_portal_templates.xml",
        "views/website_oca_integrator_data.xml",
        "views/view_res_partner.xml",
        "views/view_odoo_author.xml",
        "data/ir_cron.xml",
    ],
    "demo": [
        "demo/assets.xml",
        "demo/res_users.xml",
        "demo/res_partner.xml",
        "demo/odoo_author.xml",
        "demo/product_template_demo.xml",
        "demo/odoo_module_demo.xml",
        "demo/product_template_post_demo.xml",
    ],
    "installable": True,
}

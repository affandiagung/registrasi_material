from odoo import http
from odoo.http import request, Controller, route


class MaterialController(Controller):

    @route('/registrasi_material/get_materials', type='json', auth='user')
    def get_materials(self, material_type=None):
        materials = request.env['registrasi.material'].sudo().search([])

        if material_type:
            materials = materials.filtered(
                lambda m: m.material_type == material_type)

        return materials.read(['material_code', 'material_name', 'material_type', 'material_buy_price', 'related_supplier'])

    @route('/registrasi_material/update_material', type='json', auth='user', methods=['POST'])
    def update_material(self, material_id, material_data):
        material = request.env['registrasi.material'].sudo().browse(
            material_id)
        material.write(material_data)

    @route('/registrasi_material/delete_material', type='json', auth='user', methods=['POST'])
    def delete_material(self, material_id):
        material = request.env['registrasi.material'].sudo().browse(
            material_id)
        material.unlink()

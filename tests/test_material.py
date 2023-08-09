from odoo.tests import common


class TestMaterial(common.TransactionCase):

    def test_create_material(self):
        Material = self.env['registrasi.material']
        supplier = self.env['res.partner'].create({'name': 'Supplier Test'})

        material = Material.create({
            'material_code': 'MAT001',
            'material_name': 'Test Material',
            'material_type': 'fabric',
            'material_buy_price': 150,
            'related_supplier': supplier.id
        })

        self.assertEqual(material.material_code, 'MAT001')

    def test_material_buy_price_constraint(self):
        Material = self.env['registrasi.material']
        supplier = self.env['res.partner'].create({'name': 'Supplier Test'})

        with self.assertRaises(ValidationError):
            Material.create({
                'material_code': 'MAT002',
                'material_name': 'Test Material 2',
                'material_type': 'fabric',
                'material_buy_price': 50,
                'related_supplier': supplier.id
            })

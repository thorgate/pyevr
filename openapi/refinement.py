class Refinement:
    @classmethod
    def run(cls):
        cls.path_holding_base_children()

    @classmethod
    def path_holding_base_children(cls):
        holding_base_children = (
            ('pyevr/openapi_client/models/forest_notice.py', 'ForestNotice'),
            ('pyevr/openapi_client/models/forest_notice_all_of.py', 'ForestNotice'),
            ('pyevr/openapi_client/models/inventory_act.py', 'InventoryAct'),
            ('pyevr/openapi_client/models/inventory_act_all_of.py', 'InventoryAct'),
            ('pyevr/openapi_client/models/consolidated_act.py', 'ConsolidatedAct'),
            ('pyevr/openapi_client/models/consolidated_act_all_of.py', 'ConsolidatedAct'),
            ('pyevr/openapi_client/models/sales_contract.py', 'SalesContract'),
            ('pyevr/openapi_client/models/sales_contract_all_of.py', 'SalesContract'),
            ('pyevr/openapi_client/models/forest_act.py', 'ForestAct'),
            ('pyevr/openapi_client/models/contract_for_transfer_of_cutting_rights.py', 'ContractForTransferOfCuttingRights'),
        )
        for child in holding_base_children:
            cls.path_holding_base_child(*child)

    @classmethod
    def path_holding_base_child(cls, file_path, type_name):
        updated = ''
        first_property_found = False

        with open(file_path) as f:
            for line in f:
                if not first_property_found and updated.endswith('    @property\n'):
                    updated += "    def type(self):\n        return self._type\n\n    @property\n"
                    first_property_found = True
                updated += line
                if updated.endswith('self.local_vars_configuration = local_vars_configuration\n\n'):
                    updated += "        self._type = '" + type_name + "'\n"
                if line == '    openapi_types = {\n':
                    updated += "        'type': 'str',\n"
                if line == '    attribute_map = {\n':
                    updated += "        'type': 'type',\n"

        with open(file_path, 'w') as f:
            f.write(updated)



if __name__ == '__main__':
    Refinement.run()

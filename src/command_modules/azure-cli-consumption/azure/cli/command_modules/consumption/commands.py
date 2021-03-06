# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from ._transformers import (transform_usage_list_output,
                            transform_reservation_summary_list_output,
                            transform_reservation_detail_list_output,
                            transform_pricesheet_show_output,
                            transform_marketplace_list_output)
from ._client_factory import (usage_details_mgmt_client_factory,
                              reservation_summary_mgmt_client_factory,
                              reservation_detail_mgmt_client_factory,
                              pricesheet_mgmt_client_factory,
                              marketplace_mgmt_client_factory)
from ._exception_handler import consumption_exception_handler
from ._validators import (validate_both_start_end_dates,
                          validate_reservation_summary)


def load_command_table(self, _):
    with self.command_group('consumption usage') as g:
        g.custom_command('list', 'cli_consumption_list_usage', transform=transform_usage_list_output,
                         exception_handler=consumption_exception_handler, validator=validate_both_start_end_dates, client_factory=usage_details_mgmt_client_factory)

    with self.command_group('consumption reservation summary') as s:
        s.custom_command('list', 'cli_consumption_list_reservation_summary', transform=transform_reservation_summary_list_output,
                         exception_handler=consumption_exception_handler, validator=validate_reservation_summary, client_factory=reservation_summary_mgmt_client_factory)

    with self.command_group('consumption reservation detail') as d:
        d.custom_command('list', 'cli_consumption_list_reservation_detail', transform=transform_reservation_detail_list_output,
                         exception_handler=consumption_exception_handler, client_factory=reservation_detail_mgmt_client_factory)

    with self.command_group('consumption pricesheet') as p:
        p.custom_command('show', 'cli_consumption_list_pricesheet_show', transform=transform_pricesheet_show_output,
                         exception_handler=consumption_exception_handler, client_factory=pricesheet_mgmt_client_factory)

    with self.command_group('consumption marketplace') as m:
        m.custom_command('list', 'cli_consumption_list_marketplace', transform=transform_marketplace_list_output,
                         exception_handler=consumption_exception_handler, validator=validate_both_start_end_dates, client_factory=marketplace_mgmt_client_factory)

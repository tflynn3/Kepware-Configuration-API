import json


def get__config_v1_project(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project".format())
	return json.loads(r.text.replace(".","_"))

def put__config_v1_project(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project".format(), json=payload)
	return r

def get_aliases(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/aliases".format())
	return json.loads(r.text.replace(".","_"))

def post_aliases(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/aliases".format(), json=payload)
	return r

def get_aliases(client, aliases_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/aliases/{}".format(aliases_name))
	return json.loads(r.text.replace(".","_"))

def put_aliases(client, payload, aliases_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/aliases/{}".format(aliases_name), json=payload)
	return r

def delete_aliases(client, aliases_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/aliases/{}".format(aliases_name))
	return json.loads(r.text.replace(".","_"))

def get_channels(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels".format())
	return json.loads(r.text.replace(".","_"))

def post_channels(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels".format(), json=payload)
	return r

def get_channels(client, channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}".format(channels_name))
	return json.loads(r.text.replace(".","_"))

def put_channels(client, payload, channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}".format(channels_name), json=payload)
	return r

def delete_channels(client, channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}".format(channels_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices(client, channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices".format(channels_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices(client, payload, channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices".format(channels_name), json=payload)
	return r

def get_channels_devices(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices(client, payload, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}".format(channels_name, devices_name), json=payload)
	return r

def delete_channels_devices(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_consumerexchangegroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_consumerexchangegroups(client, channels_name, devices_name, consumer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}".format(channels_name, devices_name, consumer_exchange_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_consumerexchangegroups(client, payload, channels_name, devices_name, consumer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}".format(channels_name, devices_name, consumer_exchange_groups_name), json=payload)
	return r

def get_channels_devices_consumerexchangegroups_consumerexchanges(client, channels_name, devices_name, consumer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges".format(channels_name, devices_name, consumer_exchange_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_consumerexchangegroups_consumerexchanges(client, payload, channels_name, devices_name, consumer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges".format(channels_name, devices_name, consumer_exchange_groups_name), json=payload)
	return r

def get_channels_devices_consumerexchangegroups_consumerexchanges(client, channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}".format(channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_consumerexchangegroups_consumerexchanges(client, payload, channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}".format(channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name), json=payload)
	return r

def delete_channels_devices_consumerexchangegroups_consumerexchanges(client, channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}".format(channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_consumerexchangegroups_consumerexchanges_ranges(client, channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}/ranges".format(channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_consumerexchangegroups_consumerexchanges_ranges(client, payload, channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}/ranges".format(channels_name, devices_name, consumer_exchange_groups_name, consumer_exchanges_name), json=payload)
	return r

def get_channels_devices_consumerexchangegroups_consumerexchanges_ranges(client, channels_name, consumer_exchange_groups_name, ranges_name, devices_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}/ranges/{}".format(channels_name, consumer_exchange_groups_name, ranges_name, devices_name, consumer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_consumerexchangegroups_consumerexchanges_ranges(client, payload, channels_name, consumer_exchange_groups_name, ranges_name, devices_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}/ranges/{}".format(channels_name, consumer_exchange_groups_name, ranges_name, devices_name, consumer_exchanges_name), json=payload)
	return r

def delete_channels_devices_consumerexchangegroups_consumerexchanges_ranges(client, channels_name, consumer_exchange_groups_name, ranges_name, devices_name, consumer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/consumer_exchange_groups/{}/consumer_exchanges/{}/ranges/{}".format(channels_name, consumer_exchange_groups_name, ranges_name, devices_name, consumer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_deviceprofiles(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/device_profiles".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_deviceprofiles(client, channels_name, devices_name, device_profiles_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/device_profiles/{}".format(channels_name, devices_name, device_profiles_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_deviceprofiles(client, payload, channels_name, devices_name, device_profiles_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/device_profiles/{}".format(channels_name, devices_name, device_profiles_name), json=payload)
	return r

def get_channels_devices_enronaddressrangegroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_enronaddressrangegroups(client, channels_name, devices_name, enron_address_range_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups/{}".format(channels_name, devices_name, enron_address_range_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_enronaddressrangegroups(client, payload, channels_name, devices_name, enron_address_range_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups/{}".format(channels_name, devices_name, enron_address_range_groups_name), json=payload)
	return r

def get_channels_devices_enronaddressrangegroups_enronaddressranges(client, channels_name, devices_name, enron_address_range_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups/{}/enron_address_ranges".format(channels_name, devices_name, enron_address_range_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_enronaddressrangegroups_enronaddressranges(client, payload, channels_name, devices_name, enron_address_range_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups/{}/enron_address_ranges".format(channels_name, devices_name, enron_address_range_groups_name), json=payload)
	return r

def get_channels_devices_enronaddressrangegroups_enronaddressranges(client, channels_name, devices_name, enron_address_ranges_name, enron_address_range_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups/{}/enron_address_ranges/{}".format(channels_name, devices_name, enron_address_ranges_name, enron_address_range_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_enronaddressrangegroups_enronaddressranges(client, payload, channels_name, devices_name, enron_address_ranges_name, enron_address_range_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups/{}/enron_address_ranges/{}".format(channels_name, devices_name, enron_address_ranges_name, enron_address_range_groups_name), json=payload)
	return r

def delete_channels_devices_enronaddressrangegroups_enronaddressranges(client, channels_name, devices_name, enron_address_ranges_name, enron_address_range_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/enron_address_range_groups/{}/enron_address_ranges/{}".format(channels_name, devices_name, enron_address_ranges_name, enron_address_range_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_enronmappinggroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_enronmappinggroups(client, channels_name, devices_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}".format(channels_name, devices_name, enron_mapping_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_enronmappinggroups(client, payload, channels_name, devices_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}".format(channels_name, devices_name, enron_mapping_groups_name), json=payload)
	return r

def get_channels_devices_enronmappinggroups_enronmappings(client, channels_name, devices_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings".format(channels_name, devices_name, enron_mapping_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_enronmappinggroups_enronmappings(client, payload, channels_name, devices_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings".format(channels_name, devices_name, enron_mapping_groups_name), json=payload)
	return r

def get_channels_devices_enronmappinggroups_enronmappings(client, channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}".format(channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_enronmappinggroups_enronmappings(client, payload, channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}".format(channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name), json=payload)
	return r

def delete_channels_devices_enronmappinggroups_enronmappings(client, channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}".format(channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_enronmappinggroups_enronmappings_enronalarms(client, channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}/enron_alarms".format(channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_enronmappinggroups_enronmappings_enronalarms(client, payload, channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}/enron_alarms".format(channels_name, devices_name, enron_mappings_name, enron_mapping_groups_name), json=payload)
	return r

def get_channels_devices_enronmappinggroups_enronmappings_enronalarms(client, channels_name, enron_mapping_groups_name, enron_alarms_name, devices_name, enron_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}/enron_alarms/{}".format(channels_name, enron_mapping_groups_name, enron_alarms_name, devices_name, enron_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_enronmappinggroups_enronmappings_enronalarms(client, payload, channels_name, enron_mapping_groups_name, enron_alarms_name, devices_name, enron_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}/enron_alarms/{}".format(channels_name, enron_mapping_groups_name, enron_alarms_name, devices_name, enron_mappings_name), json=payload)
	return r

def delete_channels_devices_enronmappinggroups_enronmappings_enronalarms(client, channels_name, enron_mapping_groups_name, enron_alarms_name, devices_name, enron_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/enron_mapping_groups/{}/enron_mappings/{}/enron_alarms/{}".format(channels_name, enron_mapping_groups_name, enron_alarms_name, devices_name, enron_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_logixconfigs(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_logixconfigs(client, channels_name, devices_name, logix_configs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs/{}".format(channels_name, devices_name, logix_configs_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_logixconfigs(client, payload, channels_name, devices_name, logix_configs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs/{}".format(channels_name, devices_name, logix_configs_name), json=payload)
	return r

def get_channels_devices_logixconfigs_logixaddresses(client, channels_name, devices_name, logix_configs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs/{}/logix_addresses".format(channels_name, devices_name, logix_configs_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_logixconfigs_logixaddresses(client, payload, channels_name, devices_name, logix_configs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs/{}/logix_addresses".format(channels_name, devices_name, logix_configs_name), json=payload)
	return r

def get_channels_devices_logixconfigs_logixaddresses(client, channels_name, devices_name, logix_configs_name, logix_addresses_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs/{}/logix_addresses/{}".format(channels_name, devices_name, logix_configs_name, logix_addresses_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_logixconfigs_logixaddresses(client, payload, channels_name, devices_name, logix_configs_name, logix_addresses_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs/{}/logix_addresses/{}".format(channels_name, devices_name, logix_configs_name, logix_addresses_name), json=payload)
	return r

def delete_channels_devices_logixconfigs_logixaddresses(client, channels_name, devices_name, logix_configs_name, logix_addresses_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/logix_configs/{}/logix_addresses/{}".format(channels_name, devices_name, logix_configs_name, logix_addresses_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups(client, payload, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}".format(channels_name, devices_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_abbtotalflowmeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/abb_totalflow_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_metergroups_abbtotalflowmeters(client, payload, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/abb_totalflow_meters".format(channels_name, devices_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_abbtotalflowmeters(client, channels_name, devices_name, abb_totalflow_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/abb_totalflow_meters/{}".format(channels_name, devices_name, abb_totalflow_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_abbtotalflowmeters(client, payload, channels_name, devices_name, abb_totalflow_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/abb_totalflow_meters/{}".format(channels_name, devices_name, abb_totalflow_meters_name, meter_groups_name), json=payload)
	return r

def delete_channels_devices_metergroups_abbtotalflowmeters(client, channels_name, devices_name, abb_totalflow_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/abb_totalflow_meters/{}".format(channels_name, devices_name, abb_totalflow_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_enronmeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/enron_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_enronmeters(client, channels_name, devices_name, enron_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/enron_meters/{}".format(channels_name, devices_name, enron_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_enronmeters(client, payload, channels_name, devices_name, enron_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/enron_meters/{}".format(channels_name, devices_name, enron_meters_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_fisherrocethernetmeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_ethernet_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_metergroups_fisherrocethernetmeters(client, payload, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_ethernet_meters".format(channels_name, devices_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_fisherrocethernetmeters(client, channels_name, devices_name, fisher_roc_ethernet_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_ethernet_meters/{}".format(channels_name, devices_name, fisher_roc_ethernet_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_fisherrocethernetmeters(client, payload, channels_name, devices_name, fisher_roc_ethernet_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_ethernet_meters/{}".format(channels_name, devices_name, fisher_roc_ethernet_meters_name, meter_groups_name), json=payload)
	return r

def delete_channels_devices_metergroups_fisherrocethernetmeters(client, channels_name, devices_name, fisher_roc_ethernet_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_ethernet_meters/{}".format(channels_name, devices_name, fisher_roc_ethernet_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_fisherrocserialmeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_serial_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_metergroups_fisherrocserialmeters(client, payload, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_serial_meters".format(channels_name, devices_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_fisherrocserialmeters(client, channels_name, devices_name, fisher_roc_serial_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_serial_meters/{}".format(channels_name, devices_name, fisher_roc_serial_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_fisherrocserialmeters(client, payload, channels_name, devices_name, fisher_roc_serial_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_serial_meters/{}".format(channels_name, devices_name, fisher_roc_serial_meters_name, meter_groups_name), json=payload)
	return r

def delete_channels_devices_metergroups_fisherrocserialmeters(client, channels_name, devices_name, fisher_roc_serial_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_roc_serial_meters/{}".format(channels_name, devices_name, fisher_roc_serial_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_fisherrocplusethernetmeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_ethernet_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_metergroups_fisherrocplusethernetmeters(client, payload, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_ethernet_meters".format(channels_name, devices_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_fisherrocplusethernetmeters(client, channels_name, devices_name, fisher_rocplus_ethernet_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_ethernet_meters/{}".format(channels_name, devices_name, fisher_rocplus_ethernet_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_fisherrocplusethernetmeters(client, payload, channels_name, devices_name, fisher_rocplus_ethernet_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_ethernet_meters/{}".format(channels_name, devices_name, fisher_rocplus_ethernet_meters_name, meter_groups_name), json=payload)
	return r

def delete_channels_devices_metergroups_fisherrocplusethernetmeters(client, channels_name, devices_name, fisher_rocplus_ethernet_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_ethernet_meters/{}".format(channels_name, devices_name, fisher_rocplus_ethernet_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_fisherrocplusserialmeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_serial_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_metergroups_fisherrocplusserialmeters(client, payload, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_serial_meters".format(channels_name, devices_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_fisherrocplusserialmeters(client, channels_name, devices_name, fisher_rocplus_serial_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_serial_meters/{}".format(channels_name, devices_name, fisher_rocplus_serial_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_fisherrocplusserialmeters(client, payload, channels_name, devices_name, fisher_rocplus_serial_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_serial_meters/{}".format(channels_name, devices_name, fisher_rocplus_serial_meters_name, meter_groups_name), json=payload)
	return r

def delete_channels_devices_metergroups_fisherrocplusserialmeters(client, channels_name, devices_name, fisher_rocplus_serial_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/fisher_rocplus_serial_meters/{}".format(channels_name, devices_name, fisher_rocplus_serial_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_meterorders(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/meter_orders".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_meterorders(client, channels_name, devices_name, meter_orders_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/meter_orders/{}".format(channels_name, devices_name, meter_orders_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_meterorders(client, payload, channels_name, devices_name, meter_orders_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/meter_orders/{}".format(channels_name, devices_name, meter_orders_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_omnimeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/omni_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_omnimeters(client, channels_name, devices_name, omni_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/omni_meters/{}".format(channels_name, devices_name, omni_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_omnimeters(client, payload, channels_name, devices_name, omni_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/omni_meters/{}".format(channels_name, devices_name, omni_meters_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_metergroups_simulatedmeters(client, channels_name, devices_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/simulated_meters".format(channels_name, devices_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_metergroups_simulatedmeters(client, channels_name, devices_name, simulated_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/simulated_meters/{}".format(channels_name, devices_name, simulated_meters_name, meter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_metergroups_simulatedmeters(client, payload, channels_name, devices_name, simulated_meters_name, meter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/meter_groups/{}/simulated_meters/{}".format(channels_name, devices_name, simulated_meters_name, meter_groups_name), json=payload)
	return r

def get_channels_devices_nameresolutiongroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_nameresolutiongroups(client, channels_name, devices_name, name_resolution_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups/{}".format(channels_name, devices_name, name_resolution_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_nameresolutiongroups(client, payload, channels_name, devices_name, name_resolution_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups/{}".format(channels_name, devices_name, name_resolution_groups_name), json=payload)
	return r

def get_channels_devices_nameresolutiongroups_nameresolutions(client, channels_name, devices_name, name_resolution_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups/{}/name_resolutions".format(channels_name, devices_name, name_resolution_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_nameresolutiongroups_nameresolutions(client, payload, channels_name, devices_name, name_resolution_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups/{}/name_resolutions".format(channels_name, devices_name, name_resolution_groups_name), json=payload)
	return r

def get_channels_devices_nameresolutiongroups_nameresolutions(client, channels_name, devices_name, name_resolutions_name, name_resolution_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups/{}/name_resolutions/{}".format(channels_name, devices_name, name_resolutions_name, name_resolution_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_nameresolutiongroups_nameresolutions(client, payload, channels_name, devices_name, name_resolutions_name, name_resolution_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups/{}/name_resolutions/{}".format(channels_name, devices_name, name_resolutions_name, name_resolution_groups_name), json=payload)
	return r

def delete_channels_devices_nameresolutiongroups_nameresolutions(client, channels_name, devices_name, name_resolutions_name, name_resolution_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/name_resolution_groups/{}/name_resolutions/{}".format(channels_name, devices_name, name_resolutions_name, name_resolution_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_omnimappinggroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_omnimappinggroups(client, channels_name, devices_name, omni_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}".format(channels_name, devices_name, omni_mapping_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_omnimappinggroups(client, payload, channels_name, devices_name, omni_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}".format(channels_name, devices_name, omni_mapping_groups_name), json=payload)
	return r

def get_channels_devices_omnimappinggroups_omnimappings(client, channels_name, devices_name, omni_mapping_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings".format(channels_name, devices_name, omni_mapping_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_omnimappinggroups_omnimappings(client, channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}".format(channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_omnimappinggroups_omnimappings(client, payload, channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}".format(channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name), json=payload)
	return r

def get_channels_devices_omnimappinggroups_omnimappings_omnigasalarms(client, channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_gas_alarms".format(channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_omnimappinggroups_omnimappings_omnigasalarms(client, payload, channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_gas_alarms".format(channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name), json=payload)
	return r

def get_channels_devices_omnimappinggroups_omnimappings_omnigasalarms(client, channels_name, omni_mapping_groups_name, omni_gas_alarms_name, omni_mappings_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_gas_alarms/{}".format(channels_name, omni_mapping_groups_name, omni_gas_alarms_name, omni_mappings_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_omnimappinggroups_omnimappings_omnigasalarms(client, payload, channels_name, omni_mapping_groups_name, omni_gas_alarms_name, omni_mappings_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_gas_alarms/{}".format(channels_name, omni_mapping_groups_name, omni_gas_alarms_name, omni_mappings_name, devices_name), json=payload)
	return r

def delete_channels_devices_omnimappinggroups_omnimappings_omnigasalarms(client, channels_name, omni_mapping_groups_name, omni_gas_alarms_name, omni_mappings_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_gas_alarms/{}".format(channels_name, omni_mapping_groups_name, omni_gas_alarms_name, omni_mappings_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_omnimappinggroups_omnimappings_omniliquidalarms(client, channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_liquid_alarms".format(channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_omnimappinggroups_omnimappings_omniliquidalarms(client, payload, channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_liquid_alarms".format(channels_name, devices_name, omni_mapping_groups_name, omni_mappings_name), json=payload)
	return r

def get_channels_devices_omnimappinggroups_omnimappings_omniliquidalarms(client, channels_name, omni_mapping_groups_name, omni_mappings_name, devices_name, omni_liquid_alarms_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_liquid_alarms/{}".format(channels_name, omni_mapping_groups_name, omni_mappings_name, devices_name, omni_liquid_alarms_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_omnimappinggroups_omnimappings_omniliquidalarms(client, payload, channels_name, omni_mapping_groups_name, omni_mappings_name, devices_name, omni_liquid_alarms_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_liquid_alarms/{}".format(channels_name, omni_mapping_groups_name, omni_mappings_name, devices_name, omni_liquid_alarms_name), json=payload)
	return r

def delete_channels_devices_omnimappinggroups_omnimappings_omniliquidalarms(client, channels_name, omni_mapping_groups_name, omni_mappings_name, devices_name, omni_liquid_alarms_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/omni_mapping_groups/{}/omni_mappings/{}/omni_liquid_alarms/{}".format(channels_name, omni_mapping_groups_name, omni_mappings_name, devices_name, omni_liquid_alarms_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_producerexchangegroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_producerexchangegroups(client, channels_name, devices_name, producer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}".format(channels_name, devices_name, producer_exchange_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_producerexchangegroups(client, payload, channels_name, devices_name, producer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}".format(channels_name, devices_name, producer_exchange_groups_name), json=payload)
	return r

def get_channels_devices_producerexchangegroups_producerexchanges(client, channels_name, devices_name, producer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges".format(channels_name, devices_name, producer_exchange_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_producerexchangegroups_producerexchanges(client, payload, channels_name, devices_name, producer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges".format(channels_name, devices_name, producer_exchange_groups_name), json=payload)
	return r

def get_channels_devices_producerexchangegroups_producerexchanges(client, channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}".format(channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_producerexchangegroups_producerexchanges(client, payload, channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}".format(channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name), json=payload)
	return r

def delete_channels_devices_producerexchangegroups_producerexchanges(client, channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}".format(channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_producerexchangegroups_producerexchanges_ranges(client, channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}/ranges".format(channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_producerexchangegroups_producerexchanges_ranges(client, payload, channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}/ranges".format(channels_name, devices_name, producer_exchange_groups_name, producer_exchanges_name), json=payload)
	return r

def get_channels_devices_producerexchangegroups_producerexchanges_ranges(client, channels_name, ranges_name, producer_exchanges_name, devices_name, producer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}/ranges/{}".format(channels_name, ranges_name, producer_exchanges_name, devices_name, producer_exchange_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_producerexchangegroups_producerexchanges_ranges(client, payload, channels_name, ranges_name, producer_exchanges_name, devices_name, producer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}/ranges/{}".format(channels_name, ranges_name, producer_exchanges_name, devices_name, producer_exchange_groups_name), json=payload)
	return r

def delete_channels_devices_producerexchangegroups_producerexchanges_ranges(client, channels_name, ranges_name, producer_exchanges_name, devices_name, producer_exchange_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/producer_exchange_groups/{}/producer_exchanges/{}/ranges/{}".format(channels_name, ranges_name, producer_exchanges_name, devices_name, producer_exchange_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_services(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_services(client, channels_name, devices_name, services_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}".format(channels_name, devices_name, services_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_services(client, payload, channels_name, devices_name, services_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}".format(channels_name, devices_name, services_name), json=payload)
	return r

def get_channels_devices_services_jobs(client, channels_name, devices_name, services_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}/jobs".format(channels_name, devices_name, services_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_services_jobs(client, channels_name, devices_name, services_name, jobs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}/jobs/{}".format(channels_name, devices_name, services_name, jobs_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_services_jobs_results(client, channels_name, devices_name, services_name, jobs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}/jobs/{}/results".format(channels_name, devices_name, services_name, jobs_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_services_jobs_results(client, channels_name, services_name, results_name, jobs_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}/jobs/{}/results/{}".format(channels_name, services_name, results_name, jobs_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_services_jobs_results_readonlytags(client, channels_name, services_name, results_name, jobs_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}/jobs/{}/results/{}/readonly_tags".format(channels_name, services_name, results_name, jobs_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_services_jobs_results_readonlytags(client, channels_name, readonly_tags_name, services_name, results_name, jobs_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/services/{}/jobs/{}/results/{}/readonly_tags/{}".format(channels_name, readonly_tags_name, services_name, results_name, jobs_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_taggroups(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_taggroups(client, payload, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups".format(channels_name, devices_name), json=payload)
	return r

def get_channels_devices_taggroups(client, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}".format(channels_name, devices_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_taggroups(client, payload, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}".format(channels_name, devices_name, tag_groups_name), json=payload)
	return r

def delete_channels_devices_taggroups(client, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}".format(channels_name, devices_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_taggroups_taggroups(client, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tag_groups".format(channels_name, devices_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_taggroups_taggroups(client, payload, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tag_groups".format(channels_name, devices_name, tag_groups_name), json=payload)
	return r

def get_channels_devices_taggroups_taggroups(client, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tag_groups/{}".format(channels_name, devices_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_taggroups_taggroups(client, payload, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tag_groups/{}".format(channels_name, devices_name, tag_groups_name), json=payload)
	return r

def delete_channels_devices_taggroups_taggroups(client, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tag_groups/{}".format(channels_name, devices_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_taggroups_tags(client, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tags".format(channels_name, devices_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_taggroups_tags(client, payload, channels_name, devices_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tags".format(channels_name, devices_name, tag_groups_name), json=payload)
	return r

def get_channels_devices_taggroups_tags(client, channels_name, devices_name, tags_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tags/{}".format(channels_name, devices_name, tags_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_taggroups_tags(client, payload, channels_name, devices_name, tags_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tags/{}".format(channels_name, devices_name, tags_name, tag_groups_name), json=payload)
	return r

def delete_channels_devices_taggroups_tags(client, channels_name, devices_name, tags_name, tag_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/tag_groups/{}/tags/{}".format(channels_name, devices_name, tags_name, tag_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_devices_tags(client, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tags".format(channels_name, devices_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_devices_tags(client, payload, channels_name, devices_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/devices/{}/tags".format(channels_name, devices_name), json=payload)
	return r

def get_channels_devices_tags(client, channels_name, devices_name, tags_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/devices/{}/tags/{}".format(channels_name, devices_name, tags_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_devices_tags(client, payload, channels_name, devices_name, tags_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/devices/{}/tags/{}".format(channels_name, devices_name, tags_name), json=payload)
	return r

def delete_channels_devices_tags(client, channels_name, devices_name, tags_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/devices/{}/tags/{}".format(channels_name, devices_name, tags_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_phonebooks(client, channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/phonebooks".format(channels_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_phonebooks(client, channels_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/phonebooks/{}".format(channels_name, phonebooks_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_phonebooks(client, payload, channels_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/phonebooks/{}".format(channels_name, phonebooks_name), json=payload)
	return r

def get_channels_phonebooks_phonelist(client, channels_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonelist".format(channels_name, phonebooks_name))
	return json.loads(r.text.replace(".","_"))

def post_channels_phonebooks_phonelist(client, payload, channels_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonelist".format(channels_name, phonebooks_name), json=payload)
	return r

def get_channels_phonebooks_phonelist(client, channels_name, phonelist_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonelist/{}".format(channels_name, phonelist_name, phonebooks_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_phonebooks_phonelist(client, payload, channels_name, phonelist_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonelist/{}".format(channels_name, phonelist_name, phonebooks_name), json=payload)
	return r

def delete_channels_phonebooks_phonelist(client, channels_name, phonelist_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonelist/{}".format(channels_name, phonelist_name, phonebooks_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_phonebooks_phonepriorities(client, channels_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonepriorities".format(channels_name, phonebooks_name))
	return json.loads(r.text.replace(".","_"))

def get_channels_phonebooks_phonepriorities(client, channels_name, phonepriorities_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonepriorities/{}".format(channels_name, phonepriorities_name, phonebooks_name))
	return json.loads(r.text.replace(".","_"))

def put_channels_phonebooks_phonepriorities(client, payload, channels_name, phonepriorities_name, phonebooks_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/channels/{}/phonebooks/{}/phonepriorities/{}".format(channels_name, phonepriorities_name, phonebooks_name), json=payload)
	return r

def get_clientinterfaces(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/client_interfaces".format())
	return json.loads(r.text.replace(".","_"))

def get_clientinterfaces(client, client_interfaces_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/client_interfaces/{}".format(client_interfaces_name))
	return json.loads(r.text.replace(".","_"))

def put_clientinterfaces(client, payload, client_interfaces_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/client_interfaces/{}".format(client_interfaces_name), json=payload)
	return r

def get_services(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services".format())
	return json.loads(r.text.replace(".","_"))

def get_services(client, services_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services/{}".format(services_name))
	return json.loads(r.text.replace(".","_"))

def put_services(client, payload, services_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/services/{}".format(services_name), json=payload)
	return r

def get_services_jobs(client, services_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services/{}/jobs".format(services_name))
	return json.loads(r.text.replace(".","_"))

def get_services_jobs(client, services_name, jobs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services/{}/jobs/{}".format(services_name, jobs_name))
	return json.loads(r.text.replace(".","_"))

def get_services_jobs_results(client, services_name, jobs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services/{}/jobs/{}/results".format(services_name, jobs_name))
	return json.loads(r.text.replace(".","_"))

def get_services_jobs_results(client, results_name, services_name, jobs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services/{}/jobs/{}/results/{}".format(results_name, services_name, jobs_name))
	return json.loads(r.text.replace(".","_"))

def get_services_jobs_results_readonlytags(client, results_name, services_name, jobs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services/{}/jobs/{}/results/{}/readonly_tags".format(results_name, services_name, jobs_name))
	return json.loads(r.text.replace(".","_"))

def get_services_jobs_results_readonlytags(client, readonly_tags_name, results_name, services_name, jobs_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/services/{}/jobs/{}/results/{}/readonly_tags/{}".format(readonly_tags_name, results_name, services_name, jobs_name))
	return json.loads(r.text.replace(".","_"))

def get_uconglobaldata(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/uconglobaldata".format())
	return json.loads(r.text.replace(".","_"))

def get_uconglobaldata(client, uconglobaldata_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/uconglobaldata/{}".format(uconglobaldata_name))
	return json.loads(r.text.replace(".","_"))

def put_uconglobaldata(client, payload, uconglobaldata_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/uconglobaldata/{}".format(uconglobaldata_name), json=payload)
	return r

def get_efmexporter(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter".format())
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups".format())
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups".format(), json=payload)
	return r

def get_efmexporter_pollgroups(client, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}".format(poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups(client, payload, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}".format(poll_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups(client, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}".format(poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups(client, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups".format(poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups(client, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}".format(efm_meter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups(client, payload, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}".format(efm_meter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups(client, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups".format(efm_meter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcalexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcalexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcalexporters(client, flow_cal_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_exporters/{}".format(flow_cal_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcalexporters(client, payload, flow_cal_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_exporters/{}".format(flow_cal_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcalexporters(client, flow_cal_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_exporters/{}".format(flow_cal_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcaltxqexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_txq_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcaltxqexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_txq_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcaltxqexporters(client, flow_cal_txq_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_txq_exporters/{}".format(flow_cal_txq_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcaltxqexporters(client, payload, flow_cal_txq_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_txq_exporters/{}".format(flow_cal_txq_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_flowcaltxqexporters(client, flow_cal_txq_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/flow_cal_txq_exporters/{}".format(flow_cal_txq_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups(client, payload, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups_csvalarmmappings(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups_csvalarmmappings(client, payload, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups_csvalarmmappings(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_alarm_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_alarm_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups_csvalarmmappings(client, payload, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_alarm_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_alarm_mappings_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvalarmgroups_csvalarmmappings(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_alarm_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_alarm_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups(client, payload, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups_csvconfiggasmappings(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups/{}/csv_config_gas_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups_csvconfiggasmappings(client, payload, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups/{}/csv_config_gas_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups_csvconfiggasmappings(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name, csv_config_gas_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups/{}/csv_config_gas_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name, csv_config_gas_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups_csvconfiggasmappings(client, payload, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name, csv_config_gas_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups/{}/csv_config_gas_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name, csv_config_gas_mappings_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvconfiggasgroups_csvconfiggasmappings(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name, csv_config_gas_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_config_gas_groups/{}/csv_config_gas_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_config_gas_groups_name, csv_config_gas_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups(client, payload, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups_csveventmappings(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups_csveventmappings(client, payload, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups_csveventmappings(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_event_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_event_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups_csveventmappings(client, payload, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_event_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_event_mappings_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csveventgroups_csveventmappings(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_event_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_event_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name, gas_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups(client, payload, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups_csvhistorygasmappings(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups/{}/csv_history_gas_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups_csvhistorygasmappings(client, payload, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups/{}/csv_history_gas_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups_csvhistorygasmappings(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name, csv_history_gas_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups/{}/csv_history_gas_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name, csv_history_gas_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups_csvhistorygasmappings(client, payload, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name, csv_history_gas_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups/{}/csv_history_gas_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name, csv_history_gas_mappings_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gascsvexporters_csvhistorygasgroups_csvhistorygasmappings(client, efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name, csv_history_gas_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_csv_exporters/{}/csv_history_gas_groups/{}/csv_history_gas_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, gas_csv_exporters_name, poll_groups_name, csv_history_gas_groups_name, csv_history_gas_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters(client, gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}".format(gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters(client, payload, gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}".format(gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters(client, gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}".format(gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups(client, gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups".format(gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups(client, payload, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups_databasealarmmappings(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups_databasealarmmappings(client, payload, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups_databasealarmmappings(client, database_alarm_mappings_name, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings/{}".format(database_alarm_mappings_name, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups_databasealarmmappings(client, payload, database_alarm_mappings_name, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings/{}".format(database_alarm_mappings_name, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasealarmgroups_databasealarmmappings(client, database_alarm_mappings_name, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings/{}".format(database_alarm_mappings_name, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups(client, gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups".format(gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups(client, payload, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups_databaseconfiggasmappings(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups/{}/database_config_gas_mappings".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups_databaseconfiggasmappings(client, payload, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups/{}/database_config_gas_mappings".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups_databaseconfiggasmappings(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_mappings_name, database_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups/{}/database_config_gas_mappings/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_mappings_name, database_config_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups_databaseconfiggasmappings(client, payload, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_mappings_name, database_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups/{}/database_config_gas_mappings/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_mappings_name, database_config_gas_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseconfiggasgroups_databaseconfiggasmappings(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_mappings_name, database_config_gas_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_config_gas_groups/{}/database_config_gas_mappings/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_gas_mappings_name, database_config_gas_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups(client, gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups".format(gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups(client, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups/{}".format(efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups(client, payload, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups/{}".format(efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups_databaseeventmappings(client, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups/{}/database_event_mappings".format(efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups_databaseeventmappings(client, payload, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups/{}/database_event_mappings".format(efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups_databaseeventmappings(client, database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups/{}/database_event_mappings/{}".format(database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups_databaseeventmappings(client, payload, database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups/{}/database_event_mappings/{}".format(database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databaseeventgroups_databaseeventmappings(client, database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_event_groups/{}/database_event_mappings/{}".format(database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, gas_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups(client, gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups".format(gas_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups(client, payload, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups/{}".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups_databasehistorygasmappings(client, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups/{}/database_history_gas_mappings".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups_databasehistorygasmappings(client, payload, efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups/{}/database_history_gas_mappings".format(efm_meter_groups_name, gas_database_exporters_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups_databasehistorygasmappings(client, efm_meter_groups_name, gas_database_exporters_name, database_history_gas_mappings_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups/{}/database_history_gas_mappings/{}".format(efm_meter_groups_name, gas_database_exporters_name, database_history_gas_mappings_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups_databasehistorygasmappings(client, payload, efm_meter_groups_name, gas_database_exporters_name, database_history_gas_mappings_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups/{}/database_history_gas_mappings/{}".format(efm_meter_groups_name, gas_database_exporters_name, database_history_gas_mappings_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_gasdatabaseexporters_databasehistorygasgroups_databasehistorygasmappings(client, efm_meter_groups_name, gas_database_exporters_name, database_history_gas_mappings_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/gas_database_exporters/{}/database_history_gas_groups/{}/database_history_gas_mappings/{}".format(efm_meter_groups_name, gas_database_exporters_name, database_history_gas_mappings_name, efm_exporter_groups_name, database_history_gas_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters(client, payload, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups(client, payload, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups_csvalarmmappings(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups_csvalarmmappings(client, payload, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups_csvalarmmappings(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, csv_alarm_mappings_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, csv_alarm_mappings_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups_csvalarmmappings(client, payload, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, csv_alarm_mappings_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, csv_alarm_mappings_name, liquid_csv_exporters_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvalarmgroups_csvalarmmappings(client, efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, csv_alarm_mappings_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_alarm_groups/{}/csv_alarm_mappings/{}".format(efm_meter_groups_name, csv_alarm_groups_name, efm_exporter_groups_name, poll_groups_name, csv_alarm_mappings_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups(client, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups(client, payload, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups_csvbatchmappings(client, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups/{}/csv_batch_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups_csvbatchmappings(client, payload, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups/{}/csv_batch_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups_csvbatchmappings(client, csv_batch_mappings_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups/{}/csv_batch_mappings/{}".format(csv_batch_mappings_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups_csvbatchmappings(client, payload, csv_batch_mappings_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups/{}/csv_batch_mappings/{}".format(csv_batch_mappings_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvbatchgroups_csvbatchmappings(client, csv_batch_mappings_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_batch_groups/{}/csv_batch_mappings/{}".format(csv_batch_mappings_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups(client, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups(client, payload, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups/{}".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups_csvconfigliquidmappings(client, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups/{}/csv_config_liquid_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups_csvconfigliquidmappings(client, payload, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups/{}/csv_config_liquid_mappings".format(efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups_csvconfigliquidmappings(client, efm_meter_groups_name, efm_exporter_groups_name, csv_config_liquid_mappings_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups/{}/csv_config_liquid_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, csv_config_liquid_mappings_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups_csvconfigliquidmappings(client, payload, efm_meter_groups_name, efm_exporter_groups_name, csv_config_liquid_mappings_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups/{}/csv_config_liquid_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, csv_config_liquid_mappings_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvconfigliquidgroups_csvconfigliquidmappings(client, efm_meter_groups_name, efm_exporter_groups_name, csv_config_liquid_mappings_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_config_liquid_groups/{}/csv_config_liquid_mappings/{}".format(efm_meter_groups_name, efm_exporter_groups_name, csv_config_liquid_mappings_name, poll_groups_name, csv_config_liquid_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups(client, payload, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups_csveventmappings(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups_csveventmappings(client, payload, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups_csveventmappings(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_event_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_event_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups_csveventmappings(client, payload, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_event_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_event_mappings_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csveventgroups_csveventmappings(client, efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_event_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_event_groups/{}/csv_event_mappings/{}".format(efm_meter_groups_name, csv_event_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_event_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups(client, efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups/{}".format(efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups(client, payload, efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups/{}".format(efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups_csvhistoryliquidmappings(client, efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups/{}/csv_history_liquid_mappings".format(efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups_csvhistoryliquidmappings(client, payload, efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups/{}/csv_history_liquid_mappings".format(efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups_csvhistoryliquidmappings(client, efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_history_liquid_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups/{}/csv_history_liquid_mappings/{}".format(efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_history_liquid_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups_csvhistoryliquidmappings(client, payload, efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_history_liquid_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups/{}/csv_history_liquid_mappings/{}".format(efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_history_liquid_mappings_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvhistoryliquidgroups_csvhistoryliquidmappings(client, efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_history_liquid_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_history_liquid_groups/{}/csv_history_liquid_mappings/{}".format(efm_meter_groups_name, csv_history_liquid_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name, csv_history_liquid_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups(client, liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups".format(liquid_csv_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups(client, csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups/{}".format(csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups(client, payload, csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups/{}".format(csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups_csvliquidproductmappings(client, csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups/{}/csv_liquid_product_mappings".format(csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups_csvliquidproductmappings(client, payload, csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups/{}/csv_liquid_product_mappings".format(csv_liquid_product_groups_name, efm_meter_groups_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups_csvliquidproductmappings(client, csv_liquid_product_groups_name, efm_meter_groups_name, csv_liquid_product_mappings_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups/{}/csv_liquid_product_mappings/{}".format(csv_liquid_product_groups_name, efm_meter_groups_name, csv_liquid_product_mappings_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups_csvliquidproductmappings(client, payload, csv_liquid_product_groups_name, efm_meter_groups_name, csv_liquid_product_mappings_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups/{}/csv_liquid_product_mappings/{}".format(csv_liquid_product_groups_name, efm_meter_groups_name, csv_liquid_product_mappings_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquidcsvexporters_csvliquidproductgroups_csvliquidproductmappings(client, csv_liquid_product_groups_name, efm_meter_groups_name, csv_liquid_product_mappings_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_csv_exporters/{}/csv_liquid_product_groups/{}/csv_liquid_product_mappings/{}".format(csv_liquid_product_groups_name, efm_meter_groups_name, csv_liquid_product_mappings_name, efm_exporter_groups_name, poll_groups_name, liquid_csv_exporters_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters(client, payload, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups_databasealarmmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups_databasealarmmappings(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups_databasealarmmappings(client, database_alarm_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings/{}".format(database_alarm_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups_databasealarmmappings(client, payload, database_alarm_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings/{}".format(database_alarm_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasealarmgroups_databasealarmmappings(client, database_alarm_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_alarm_groups/{}/database_alarm_mappings/{}".format(database_alarm_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_alarm_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups_databasebatchmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups/{}/database_batch_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups_databasebatchmappings(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups/{}/database_batch_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups_databasebatchmappings(client, database_batch_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups/{}/database_batch_mappings/{}".format(database_batch_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups_databasebatchmappings(client, payload, database_batch_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups/{}/database_batch_mappings/{}".format(database_batch_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasebatchgroups_databasebatchmappings(client, database_batch_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_batch_groups/{}/database_batch_mappings/{}".format(database_batch_mappings_name, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_batch_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups(client, efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups/{}".format(efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups(client, payload, efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups/{}".format(efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups_databaseconfigliquidmappings(client, efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups/{}/database_config_liquid_mappings".format(efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups_databaseconfigliquidmappings(client, payload, efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups/{}/database_config_liquid_mappings".format(efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups_databaseconfigliquidmappings(client, efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_liquid_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups/{}/database_config_liquid_mappings/{}".format(efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_liquid_mappings_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups_databaseconfigliquidmappings(client, payload, efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_liquid_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups/{}/database_config_liquid_mappings/{}".format(efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_liquid_mappings_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseconfigliquidgroups_databaseconfigliquidmappings(client, efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_liquid_mappings_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_config_liquid_groups/{}/database_config_liquid_mappings/{}".format(efm_meter_groups_name, database_config_liquid_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_config_liquid_mappings_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups(client, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups/{}".format(efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups(client, payload, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups/{}".format(efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups_databaseeventmappings(client, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups/{}/database_event_mappings".format(efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups_databaseeventmappings(client, payload, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups/{}/database_event_mappings".format(efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups_databaseeventmappings(client, database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups/{}/database_event_mappings/{}".format(database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups_databaseeventmappings(client, payload, database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups/{}/database_event_mappings/{}".format(database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseeventgroups_databaseeventmappings(client, database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_event_groups/{}/database_event_mappings/{}".format(database_event_mappings_name, efm_meter_groups_name, database_event_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups_databasehistoryliquidmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups/{}/database_history_liquid_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups_databasehistoryliquidmappings(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups/{}/database_history_liquid_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups_databasehistoryliquidmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_mappings_name, database_history_liquid_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups/{}/database_history_liquid_mappings/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_mappings_name, database_history_liquid_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups_databasehistoryliquidmappings(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_mappings_name, database_history_liquid_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups/{}/database_history_liquid_mappings/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_mappings_name, database_history_liquid_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databasehistoryliquidgroups_databasehistoryliquidmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_mappings_name, database_history_liquid_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_history_liquid_groups/{}/database_history_liquid_mappings/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_history_liquid_mappings_name, database_history_liquid_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups(client, liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups".format(liquid_database_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups_databaseliquidproductmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups/{}/database_liquid_product_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups_databaseliquidproductmappings(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups/{}/database_liquid_product_mappings".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, poll_groups_name, database_liquid_product_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups_databaseliquidproductmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_liquid_product_mappings_name, poll_groups_name, database_liquid_product_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups/{}/database_liquid_product_mappings/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_liquid_product_mappings_name, poll_groups_name, database_liquid_product_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups_databaseliquidproductmappings(client, payload, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_liquid_product_mappings_name, poll_groups_name, database_liquid_product_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups/{}/database_liquid_product_mappings/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_liquid_product_mappings_name, poll_groups_name, database_liquid_product_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_liquiddatabaseexporters_databaseliquidproductgroups_databaseliquidproductmappings(client, efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_liquid_product_mappings_name, poll_groups_name, database_liquid_product_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/liquid_database_exporters/{}/database_liquid_product_groups/{}/database_liquid_product_mappings/{}".format(efm_meter_groups_name, liquid_database_exporters_name, efm_exporter_groups_name, database_liquid_product_mappings_name, poll_groups_name, database_liquid_product_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_pgasexporters(client, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/pgas_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmexportergroups_pgasexporters(client, payload, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/pgas_exporters".format(efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmexportergroups_pgasexporters(client, pgas_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/pgas_exporters/{}".format(pgas_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmexportergroups_pgasexporters(client, payload, pgas_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/pgas_exporters/{}".format(pgas_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmexportergroups_pgasexporters(client, pgas_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_exporter_groups/{}/pgas_exporters/{}".format(pgas_exporters_name, efm_meter_groups_name, poll_groups_name, efm_exporter_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_efmexporter_pollgroups_efmmetergroups_efmmeters(client, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_meters".format(efm_meter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def post_efmexporter_pollgroups_efmmetergroups_efmmeters(client, payload, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_meters".format(efm_meter_groups_name, poll_groups_name), json=payload)
	return r

def get_efmexporter_pollgroups_efmmetergroups_efmmeters(client, efm_meters_name, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_meters/{}".format(efm_meters_name, efm_meter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def put_efmexporter_pollgroups_efmmetergroups_efmmeters(client, payload, efm_meters_name, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_meters/{}".format(efm_meters_name, efm_meter_groups_name, poll_groups_name), json=payload)
	return r

def delete_efmexporter_pollgroups_efmmetergroups_efmmeters(client, efm_meters_name, efm_meter_groups_name, poll_groups_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_efmexporter/poll_groups/{}/efm_meter_groups/{}/efm_meters/{}".format(efm_meters_name, efm_meter_groups_name, poll_groups_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway".format())
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_mqttclients(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/mqtt_clients".format())
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_mqttclients(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/mqtt_clients".format(), json=payload)
	return r

def get_iotgateway_mqttclients(client, mqtt_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}".format(mqtt_clients_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_mqttclients(client, payload, mqtt_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}".format(mqtt_clients_name), json=payload)
	return r

def delete_iotgateway_mqttclients(client, mqtt_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}".format(mqtt_clients_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_mqttclients_iotitems(client, mqtt_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}/iot_items".format(mqtt_clients_name))
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_mqttclients_iotitems(client, payload, mqtt_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}/iot_items".format(mqtt_clients_name), json=payload)
	return r

def get_iotgateway_mqttclients_iotitems(client, mqtt_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}/iot_items/{}".format(mqtt_clients_name, iot_items_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_mqttclients_iotitems(client, payload, mqtt_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}/iot_items/{}".format(mqtt_clients_name, iot_items_name), json=payload)
	return r

def delete_iotgateway_mqttclients_iotitems(client, mqtt_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/mqtt_clients/{}/iot_items/{}".format(mqtt_clients_name, iot_items_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_restclients(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_clients".format())
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_restclients(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/rest_clients".format(), json=payload)
	return r

def get_iotgateway_restclients(client, rest_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}".format(rest_clients_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_restclients(client, payload, rest_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}".format(rest_clients_name), json=payload)
	return r

def delete_iotgateway_restclients(client, rest_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}".format(rest_clients_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_restclients_iotitems(client, rest_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}/iot_items".format(rest_clients_name))
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_restclients_iotitems(client, payload, rest_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}/iot_items".format(rest_clients_name), json=payload)
	return r

def get_iotgateway_restclients_iotitems(client, rest_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}/iot_items/{}".format(rest_clients_name, iot_items_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_restclients_iotitems(client, payload, rest_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}/iot_items/{}".format(rest_clients_name, iot_items_name), json=payload)
	return r

def delete_iotgateway_restclients_iotitems(client, rest_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/rest_clients/{}/iot_items/{}".format(rest_clients_name, iot_items_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_restservers(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_servers".format())
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_restservers(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/rest_servers".format(), json=payload)
	return r

def get_iotgateway_restservers(client, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}".format(rest_servers_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_restservers(client, payload, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}".format(rest_servers_name), json=payload)
	return r

def delete_iotgateway_restservers(client, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}".format(rest_servers_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_restservers_iotitems(client, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}/iot_items".format(rest_servers_name))
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_restservers_iotitems(client, payload, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}/iot_items".format(rest_servers_name), json=payload)
	return r

def get_iotgateway_restservers_iotitems(client, iot_items_name, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}/iot_items/{}".format(iot_items_name, rest_servers_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_restservers_iotitems(client, payload, iot_items_name, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}/iot_items/{}".format(iot_items_name, rest_servers_name), json=payload)
	return r

def delete_iotgateway_restservers_iotitems(client, iot_items_name, rest_servers_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/rest_servers/{}/iot_items/{}".format(iot_items_name, rest_servers_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_thingworxclients(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/thingworx_clients".format())
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_thingworxclients(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/thingworx_clients".format(), json=payload)
	return r

def get_iotgateway_thingworxclients(client, thingworx_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}".format(thingworx_clients_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_thingworxclients(client, payload, thingworx_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}".format(thingworx_clients_name), json=payload)
	return r

def delete_iotgateway_thingworxclients(client, thingworx_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}".format(thingworx_clients_name))
	return json.loads(r.text.replace(".","_"))

def get_iotgateway_thingworxclients_iotitems(client, thingworx_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}/iot_items".format(thingworx_clients_name))
	return json.loads(r.text.replace(".","_"))

def post_iotgateway_thingworxclients_iotitems(client, payload, thingworx_clients_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}/iot_items".format(thingworx_clients_name), json=payload)
	return r

def get_iotgateway_thingworxclients_iotitems(client, thingworx_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}/iot_items/{}".format(thingworx_clients_name, iot_items_name))
	return json.loads(r.text.replace(".","_"))

def put_iotgateway_thingworxclients_iotitems(client, payload, thingworx_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}/iot_items/{}".format(thingworx_clients_name, iot_items_name), json=payload)
	return r

def delete_iotgateway_thingworxclients_iotitems(client, thingworx_clients_name, iot_items_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_iot_gateway/thingworx_clients/{}/iot_items/{}".format(thingworx_clients_name, iot_items_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler".format())
	return json.loads(r.text.replace(".","_"))

def get_scheduler_priorities(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/priorities".format())
	return json.loads(r.text.replace(".","_"))

def get_scheduler_priorities(client, priorities_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/priorities/{}".format(priorities_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_priorities(client, payload, priorities_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/priorities/{}".format(priorities_name), json=payload)
	return r

def get_scheduler_schedules(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules".format())
	return json.loads(r.text.replace(".","_"))

def post_scheduler_schedules(client, payload, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_scheduler/schedules".format(), json=payload)
	return r

def get_scheduler_schedules(client, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}".format(schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules(client, payload, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}".format(schedules_name), json=payload)
	return r

def delete_scheduler_schedules(client, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_scheduler/schedules/{}".format(schedules_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_exceptiongroups(client, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups".format(schedules_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_exceptiongroups(client, exception_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups/{}".format(exception_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_exceptiongroups(client, payload, exception_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups/{}".format(exception_groups_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_exceptiongroups_pollexceptions(client, exception_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups/{}/poll_exceptions".format(exception_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def post_scheduler_schedules_exceptiongroups_pollexceptions(client, payload, exception_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups/{}/poll_exceptions".format(exception_groups_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_exceptiongroups_pollexceptions(client, poll_exceptions_name, exception_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups/{}/poll_exceptions/{}".format(poll_exceptions_name, exception_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_exceptiongroups_pollexceptions(client, payload, poll_exceptions_name, exception_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups/{}/poll_exceptions/{}".format(poll_exceptions_name, exception_groups_name, schedules_name), json=payload)
	return r

def delete_scheduler_schedules_exceptiongroups_pollexceptions(client, poll_exceptions_name, exception_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_scheduler/schedules/{}/exception_groups/{}/poll_exceptions/{}".format(poll_exceptions_name, exception_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_realtimeobjects(client, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects".format(schedules_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_realtimeobjects(client, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}".format(real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_realtimeobjects(client, payload, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}".format(real_time_objects_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_realtimeobjects_schedulerchannels(client, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels".format(real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def post_scheduler_schedules_realtimeobjects_schedulerchannels(client, payload, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels".format(real_time_objects_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_realtimeobjects_schedulerchannels(client, scheduler_channels_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}".format(scheduler_channels_name, real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_realtimeobjects_schedulerchannels(client, payload, scheduler_channels_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}".format(scheduler_channels_name, real_time_objects_name, schedules_name), json=payload)
	return r

def delete_scheduler_schedules_realtimeobjects_schedulerchannels(client, scheduler_channels_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}".format(scheduler_channels_name, real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices(client, scheduler_channels_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices".format(scheduler_channels_name, real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def post_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices(client, payload, scheduler_channels_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices".format(scheduler_channels_name, real_time_objects_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices(client, scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}".format(scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices(client, payload, scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}".format(scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name), json=payload)
	return r

def delete_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices(client, scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}".format(scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices_schedulertags(client, scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}/scheduler_tags".format(scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def post_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices_schedulertags(client, payload, scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}/scheduler_tags".format(scheduler_channels_name, scheduler_devices_name, real_time_objects_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices_schedulertags(client, real_time_objects_name, scheduler_devices_name, scheduler_tags_name, schedules_name, scheduler_channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}/scheduler_tags/{}".format(real_time_objects_name, scheduler_devices_name, scheduler_tags_name, schedules_name, scheduler_channels_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices_schedulertags(client, payload, real_time_objects_name, scheduler_devices_name, scheduler_tags_name, schedules_name, scheduler_channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}/scheduler_tags/{}".format(real_time_objects_name, scheduler_devices_name, scheduler_tags_name, schedules_name, scheduler_channels_name), json=payload)
	return r

def delete_scheduler_schedules_realtimeobjects_schedulerchannels_schedulerdevices_schedulertags(client, real_time_objects_name, scheduler_devices_name, scheduler_tags_name, schedules_name, scheduler_channels_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_scheduler/schedules/{}/real_time_objects/{}/scheduler_channels/{}/scheduler_devices/{}/scheduler_tags/{}".format(real_time_objects_name, scheduler_devices_name, scheduler_tags_name, schedules_name, scheduler_channels_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_recurrencegroups(client, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups".format(schedules_name))
	return json.loads(r.text.replace(".","_"))

def get_scheduler_schedules_recurrencegroups(client, recurrence_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups/{}".format(recurrence_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_recurrencegroups(client, payload, recurrence_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups/{}".format(recurrence_groups_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_recurrencegroups_pollrecurrences(client, recurrence_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups/{}/poll_recurrences".format(recurrence_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def post_scheduler_schedules_recurrencegroups_pollrecurrences(client, payload, recurrence_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.post(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups/{}/poll_recurrences".format(recurrence_groups_name, schedules_name), json=payload)
	return r

def get_scheduler_schedules_recurrencegroups_pollrecurrences(client, poll_recurrences_name, recurrence_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups/{}/poll_recurrences/{}".format(poll_recurrences_name, recurrence_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def put_scheduler_schedules_recurrencegroups_pollrecurrences(client, payload, poll_recurrences_name, recurrence_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.put(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups/{}/poll_recurrences/{}".format(poll_recurrences_name, recurrence_groups_name, schedules_name), json=payload)
	return r

def delete_scheduler_schedules_recurrencegroups_pollrecurrences(client, poll_recurrences_name, recurrence_groups_name, schedules_name):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.delete(base_url + "/config/v1/project/_scheduler/schedules/{}/recurrence_groups/{}/poll_recurrences/{}".format(poll_recurrences_name, recurrence_groups_name, schedules_name))
	return json.loads(r.text.replace(".","_"))

def get__config_v1_transactionlog(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/transaction_log".format())
	return json.loads(r.text.replace(".","_"))

def get__config_v1_eventlog(client, ):
	base_url = "{}{}:{}".format(client.protocol, client.address, client.port)
	r = client.session.get(base_url + "/config/v1/event_log".format())
	return json.loads(r.text.replace(".","_"))


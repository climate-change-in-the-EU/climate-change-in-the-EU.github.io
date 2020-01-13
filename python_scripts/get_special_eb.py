import requests

# IDs of the datasets we want to query --> TODO: complete, maybe list in separate file?
datasets_interesting = ['S1084_80_2_409', 'S2060_83_4_435_ENG', 'S2140_87_1_459_ENG', 'S2212_91_3_490_ENG']

# Directory for output/RDF data
dir_processed_eb_rdf = 'data/processed_data/special_eb/rdf/'


def api_request(dataset_ids):
    datasets = {}
    # Do an API request for every package specified by ID
    for dataset_id in dataset_ids:
        # Return the metadata of a dataset (package) and its resources
        # Documentation: https://app.swaggerhub.com/apis/navarde/eu-open_data_portal/0.7.0#/read/packageShowGet
        request_url = 'https://data.europa.eu/euodp/data/apiodp/action/package_show?id=' + dataset_id
        response = requests.get(request_url)
        # Use JSON/dict representation of the response
        datasets[dataset_id] = response.json()
    return datasets


def get_rdf_data(dataset_ids):
    datasets = api_request(dataset_ids)
    for dataset_id in dataset_ids:
        # Write the 'rdf' part of the response dict to an RDF file
        with open(dir_processed_eb_rdf + dataset_id + ".rdf", "w") as text_file:
            print(datasets[dataset_id]['result']['rdf'], file=text_file)


# print(datasets) ## All datasets in the response


# TODO: is it possible to figure out the download links from the response and download the newest version of the files
#  (instead of doing that by hand separatedly)?


get_rdf_data(datasets_interesting)
from deployment_utils import ManifestMaker
import os
import argparse


def write_deployment(path, contents):
    f = open(path, "w")
    f.write(contents)
    f.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Locust cluster manifest generator")
    parser.add_argument("-n", "--name", required=True, help="Name of the test cluster artifacts")
    parser.add_argument("-t", "--target_host", required=True, help="Target host to run tests against")
    parser.add_argument("-r", "--repo", required=True, help="Github repository containing the tests")
    parser.add_argument("-f", "--test_file", required=True, help="The locust file to be used, relative to the github root path")
    parser.add_argument("-s", "--size", required=False, help="Number of workers pods to be created. Default to 1", type=int, default=1)
    parser.add_argument("-o", "--output", required=False, help="Manifest files output", default=".")

    config = vars(parser.parse_args())
    maker = ManifestMaker(config)
    write_deployment(os.path.join(config["output"], config["name"]+"-locust-master.yaml"), maker.master_deployment())
    write_deployment(os.path.join(config["output"], config["name"]+"-locust-master-service.yaml"), maker.master_service())
    write_deployment(os.path.join(config["output"], config["name"]+"-locust-master-service-lb.yaml"), maker.master_service_lb())
    write_deployment(os.path.join(config["output"], config["name"]+"-locust-worker.yaml"), maker.worker_deployment())


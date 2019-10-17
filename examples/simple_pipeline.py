from shlumpy.pipeline import Pipeline

pipeline = Pipeline("cicd")


@pipeline.stage
def build_package(src='a', dest='a'):
    print("Building a package from the source code")


@pipeline.stage
def save_artifact(src='a'):
    print("Saving the package to Artifactory")


@pipeline.stage
def deploy_artifact(url='a'):
    print("Deploying latest artifact to production")


@pipeline.stage
def run_tests(url='a'):
    print("Run tests")


@pipeline.stage
def send_slack_message(url='a'):
    print("Sending a slack message about the tests")


def main():
    pipeline.order_stages("build_package", "save_artifact", "deploy_artifact",
                          "run_tests")
    pipeline.order_stages("deploy_artifact", "send_slack_message")
    pipeline.run()


if __name__ == "main":
    main()

import shlumpy


@shlumpy.stage("stage1")
def build_package(src, dest):
    print("Building a package from the source code")

@shlumpy.stage("stage2")
def save_artifact(src):
    print("Saving the package to Artifactory")

@shlumpy.stage("stage3")
def deploy_artifact(url):
    print("Deploying latest artifact to production")


fb = FlowBuilder()
fb.flow = stage1 > stage2 > stage3

with FlowRunner(fb) as fr:
    fr.run(fb)

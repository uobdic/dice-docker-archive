import os
import glob
import subprocess

version = os.environ['CMSSW_VERSION']
arch = os.environ['SCRAM_ARCH']
install_dir = os.environ['VO_CMS_SW_DIR']

env_files = glob.glob('{0}/{1}/external/apt/*/etc/profile.d/init.sh'.format(install_dir, arch))
env_file = env_files[0]
dep_command = ['bash', '-c', 'source {0} && apt-cache depends cms+cmssw+CMSSW_{1}'.format(env_file, version)]
proc = subprocess.Popen(dep_command, stdout=subprocess.PIPE)

dependencies = []
for line in proc.stdout:
    # dependencies will come as formatted as
    #   Depends: external+gcc+4.9.1-cms
    if 'Depends:' in line:
        (_, dependency) = line.split(':')
        dependency = dependency.strip()
        dependencies.append(dependency)
#         print 'RUN . ${{VO_CMS_SW_DIR}}/${{SCRAM_ARCH}}/external/apt/*/etc/profile.d/init.sh; apt-get install -y {0}'.format(dependency)
proc.communicate()
        
deps = ' '.join(dependencies)
install_command = ['bash', '-c', 'source {0} && apt-get install -y {1}'.format(env_file, deps)]
subprocess.Popen(install_command, stdout=subprocess.PIPE).communicate()

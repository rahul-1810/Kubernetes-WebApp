#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print("Access-Control-Allow-Origin: *")
print()

f = cgi.FieldStorage()
t = f.getvalue("x")
q = f.getvalue("y")
val = t.split()
if val[0] == "1":
    deployment_name = val[2]
    image_name = val[1]
    cmd = "kubectl create deployment " + (deployment_name) + " --image=" + (image_name)
    output = subprocess.getoutput( cmd + " --kubeconfig admin.conf")
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "2":
    pod_name = val[2]
    image_name = val[1]
    cmd = "kubectl run " + (pod_name) + " --image=" + (image_name)
    output = subprocess.getoutput(cmd + " --kubeconfig admin.conf")
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "3":
    pod_name = val[1]
    cmd = "kubectl delete pod " + (pod_name)
    output = subprocess.getoutput(cmd + " --kubeconfig admin.conf")
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "4":
    deployment_name = val[1]
    cmd = "kubectl delete deployment " + (deployment_name)
    output = subprocess.getoutput(cmd + " --kubeconfig admin.conf")
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "5":
    deployment_name = val[1]
    port_no = val[2]
    Expose_type =  val[3]
    cmd = "kubectl expose deployment " + (deployment_name) + " --port=" + (port_no) + " --type=" + (Expose_type)
    output = subprocess.getoutput(cmd + " --kubeconfig admin.conf")
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "6":
    deployment_name = val[1]
    replica = val[2]
    cmd = "kubectl scale deployment " + (deployment_name) + " --replicas=" + (replica)
    output = subprocess.getoutput(cmd + " --kubeconfig admin.conf")
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "7":
    cmd = "kubectl get pods --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "8":
    cmd = "kubectl get deployments --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print('<h4> <pre> {} </pre> </h4>'.format(output))

elif val[0] == "9":
    cmd = "kubectl get svc --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print('<h4> <pre> {} </pre> </h4>'.format(output))


elif val[0] == "11":
    print("<h4> I Can Help you in Setting-Up Kubernetes Resources from your Instructions. </h4>")

elif val[0] == "12":
    print("<h4 > Heyy..!! I'm Kube Bot </h4>")

elif q == "15":
    cmd = "kubectl delete all --all --kubeconfig admin.conf"
    output = subprocess.getoutput(cmd)
    print(output)


elif val[0] == "13":
    print("<h4> 192.168.99.102 </h4>")
elif val[0] == "404":
    print("Please Write Something")


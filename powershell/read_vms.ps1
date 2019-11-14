#!/usr/bin/pwsh

Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2] | Out-Null

# Cluster ermitteln
$CLUSTERS = Get-Cluster

Foreach ($CLUSTER in $CLUSTERS) {
  #"CLUSTER = '$CLUSTER'" | Tee-Object -FilePath vm_$CLUSTER.py
  "CLUSTER = '$CLUSTER'" | Out-File -FilePath vm_$CLUSTER.py
  
  $VMS = Get-VM -Location $CLUSTER

  Foreach ($VM in $VMS) {
    $NAME = $VM.Name
    "NAME = '$NAME'" | Out-File -FilePath vm_$CLUSTER.py -Append
    
    $VCPUS = $VM.NumCpu
    "VCPUS = '$VCPUS'" | Tee-Object -FilePath vm_$CLUSTER.py -Append

    $MEMORY = $VM.MemoryMB
    "MEMORY = '$MEMORY'" | Tee-Object -FilePath vm_$CLUSTER.py -Append

    $DISK = [math]::round((Get-HardDisk -vm $VM | Measure-Object -Sum CapacityGB).Sum)
    "DISK = '$DISK'" | Tee-Object -FilePath vm_$CLUSTER.py -Append

    $STATUS = $VM.PowerState
    "STATUS = '$STATUS'" | Tee-Object -FilePath vm_$CLUSTER.py -Append
 
    $ROLE = ((Get-TagAssignment -Entity $VM -Category 'Role')).Tag.Name
    IF ($ROLE) { "ROLE = '$ROLE'" | Tee-Object -FilePath vm_$CLUSTER.py -Append }

    "" | Tee-Object -FilePath vm_$CLUSTER.py -Append
  }

"" | Tee-Object -FilePath vm_$CLUSTER.py -Append
}

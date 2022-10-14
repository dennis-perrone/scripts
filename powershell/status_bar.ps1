# This is a working status bar.
for ($counter = 1; $counter -le 100; $counter++ )
{
		# ADD YOUR CODE HERE
    Write-Progress -Activity "Update Progress" -Status "$counter% Complete:" -PercentComplete $counter;
}
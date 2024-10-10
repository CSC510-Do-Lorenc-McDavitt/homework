BEGIN { FS = ","; OFS = "," } {
	print $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13
	sum += $7
}
END { print "Average age: " sum / NR }

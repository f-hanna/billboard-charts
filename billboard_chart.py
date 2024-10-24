import billboard

# Fetch the current Hot 100 chart
chart = billboard.ChartData('hot-100')
print(chart.title)  # Prints the title of the chart

# Get the no. 1 song on the chart
song = chart[0]
print(f"1. '{song.title}' by {song.artist} ({song.weeks} weeks on chart)")

# Print the entire chart
print(chart)

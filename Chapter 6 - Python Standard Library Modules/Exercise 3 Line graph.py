import matplotlib.pyplot as plot

def draw_lines():
    # Drawing a regluar line from (1, 2) to (6, 8)
    plot.plot([1, 6], [2, 8], label='Regular Line', color='blue')

    # Drawing a dotted line from (1, 3) to (2, 8) to (6, 1) to (8, 10)
    plot.plot([1, 2, 6, 8], [3, 8, 1, 10], label='Dotted Line', linestyle='dotted', color='red')

    # Axis labels
    plot.xlabel('X-axis')
    plot.ylabel('Y-axis')

    # Plot title
    plot.title('Line Diagram')

    # The legend
    plot.legend()

    # Show the plot
    plot.show()

if __name__ == "__main__":
    draw_lines()

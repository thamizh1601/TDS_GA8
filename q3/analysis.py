# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo",
# ]
# ///
# Author: 22f2000116@ds.study.iitm.ac.in
# Email: 22f2000116@ds.study.iitm.ac.in
# Interactive Data Analysis Notebook
# Contact: 22f2000116@ds.study.iitm.ac.in

import marimo

__generated_with = "0.10.6"
app = marimo.App(width="medium")


@app.cell
def header():
    # 22f2000116@ds.study.iitm.ac.in
    # This cell imports marimo and displays the header
    # No dependencies - this is the entry point
    import marimo as mo
    
    mo.md("""
    # 📊 Interactive Data Analysis
    
    **Author:** 22f2000116@ds.study.iitm.ac.in
    
    This notebook demonstrates variable relationships using interactive widgets.
    """)
    return (mo,)


@app.cell
def create_slider(mo):
    # 22f2000116@ds.study.iitm.ac.in
    # This cell creates the interactive slider widget
    # DEPENDENCY: Receives 'mo' from the header cell
    # OUTPUT: 'slider' - used by downstream cells for dynamic content
    
    slider = mo.ui.slider(
        start=1, 
        stop=100, 
        value=50, 
        label="Select a value (1-100):"
    )
    
    mo.md(f"""
    ## Interactive Controls
    
    Use the slider below to adjust the value:
    
    {slider}
    """)
    return (slider,)


@app.cell
def dynamic_output(mo, slider):
    # 22f2000116@ds.study.iitm.ac.in
    # This cell generates dynamic output based on slider value
    # DEPENDENCIES: 
    #   - 'mo' from header cell (for markdown rendering)
    #   - 'slider' from create_slider cell (for reactive value)
    # This cell automatically re-runs when slider.value changes
    
    value = slider.value
    squared = value ** 2
    cubed = value ** 3
    
    # Generate visual indicator based on value
    bar_length = int(value / 2)
    progress_bar = "█" * bar_length + "░" * (50 - bar_length)
    
    mo.md(f"""
    ## 📈 Dynamic Analysis Results
    
    **Current Value:** {value}
    
    **Progress:** [{progress_bar}] {value}%
    
    ### Calculations
    
    | Metric | Value |
    |--------|-------|
    | Input (n) | {value} |
    | Squared (n²) | {squared:,} |
    | Cubed (n³) | {cubed:,} |
    
    ### Visual Representation
    
    {'🟢' * min(value // 5, 20)} ({value})
    
    ---
    *Analysis by 22f2000116@ds.study.iitm.ac.in*
    """)
    return (cubed, squared, value,)


@app.cell
def category_analysis(mo, slider):
    # 22f2000116@ds.study.iitm.ac.in
    # This cell categorizes the slider value
    # DEPENDENCIES:
    #   - 'mo' from header cell
    #   - 'slider' from create_slider cell
    # DATA FLOW: slider.value -> category determination -> markdown output
    
    val = slider.value
    
    if val <= 25:
        category = "Low"
        emoji = "🔴"
        description = "Value is in the low range"
    elif val <= 50:
        category = "Medium-Low"
        emoji = "🟠"
        description = "Value is below average"
    elif val <= 75:
        category = "Medium-High"
        emoji = "🟡"
        description = "Value is above average"
    else:
        category = "High"
        emoji = "🟢"
        description = "Value is in the high range"
    
    mo.md(f"""
    ## 📊 Value Classification
    
    {emoji} **Category:** {category}
    
    {description}
    
    ---
    *Contact: 22f2000116@ds.study.iitm.ac.in*
    """)
    return (category,)


if __name__ == "__main__":
    app.run()

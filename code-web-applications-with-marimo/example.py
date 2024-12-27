import marimo

__generated_with = "0.10.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    x = mo.ui.slider(0, 200)
    return (x,)


@app.cell
def _(x):
    x
    return


@app.cell
def _(mo, x):
    mo.md(f"The value is {x.value}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

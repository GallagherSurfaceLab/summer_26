# Onboarding guide — Python, Git, and GitHub
 
This section provides a structured set of learning tasks to get you set up and comfortable with the tools used in this project before you start working on the analysis code.
 
---
 
# Setting up your computer

## Git, GitHub and GitHub Desktop

### Install Git
 
Git is version control software — it tracks every change you make to your code, lets you go back to previous versions, and enables collaboration.
 
- **Windows:** Download Git for Windows from [https://git-scm.com/download/win](https://git-scm.com/download/win). Accept the defaults during installation. This also installs **Git Bash**, a terminal you will use for Git commands.
- **macOS:** Run `git --version` in Terminal. If Git is not installed, macOS will prompt you to install the Xcode Command Line Tools, which includes Git.
- **Linux:** Run `sudo apt install git` (Ubuntu/Debian) or `sudo dnf install git` (Fedora).
After installation, open a terminal and configure Git with your name and email (these appear in your commit history):


### Create a GitHub account
 
GitHub is a website that hosts Git repositories online. It lets you back up your code, share it with your supervisor, and collaborate.
 
- Sign up at [https://github.com](https://github.com). Use your university email address.
- Apply for the **GitHub Student Developer Pack** at [https://education.github.com/pack](https://education.github.com/pack) — this gives you free access to GitHub Pro and other tools while you are a student.
- Download and install [GitHub Desktop](https://desktop.github.com/download/), this simplifies the Version Control workflow and allow you to work completely with in a GUI.
- Reveiw GitHub Tutorials
    - [Git, GitHub, & GitHub Desktop for beginners](https://www.youtube.com/watch?v=8Dd7KRpKeaE)
    - [git - the simple guide](https://rogerdudler.github.io/git-guide/)
    - [GitHub Docs - Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)
    - [Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)

---


## Miniconda, VS Code, and Jupyter for STM image analysis

This guide walks you through setting up a clean, reproducible Python environment
for the STM Voronoi analysis project. It uses **Miniconda** (a minimal Python
installer), **VS Code** (a code editor), and **Jupyter Notebooks** (interactive
computing). Everything here is free and works on Windows, macOS, and Linux.

By the end you will have:
- A working Python environment with all project packages installed
- VS Code configured for Python and Jupyter
- A project folder connected to Git and GitHub
- A test notebook confirming everything works

---

## Why Miniconda instead of Anaconda?

Anaconda installs hundreds of packages automatically, many of which you will
never use. Miniconda installs only Python and the `conda` package manager, and
lets you install exactly what you need. This keeps your environment smaller,
faster, and easier to understand. For a focused project like this one,
Miniconda is the better choice.

---

## Part 1 — Install Miniconda

### Windows

1. Go to [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
   and download the **Miniconda3 Windows 64-bit** installer (`.exe` file).
2. Run the installer. On the options screen:
   - Select **"Just Me"** (not "All Users")
   - Leave the install location as the default
   - **Uncheck** "Add Miniconda3 to my PATH environment variable" — this is
     intentional; you will use the dedicated **Anaconda Prompt** instead
   - Check "Register Miniconda3 as my default Python"
3. Click Install and wait for it to finish.

After installation, open **Anaconda Prompt** from the Start menu (search for
"Anaconda Prompt" — not "Anaconda Navigator"). You should see a prompt
beginning with `(base)`:

```
(base) C:\Users\YourName>
```

### macOS

1. Go to [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
   and download the **Miniconda3 macOS** installer. Choose:
   - **Apple Silicon (M1/M2/M3 Mac):** the `arm64` `.pkg` installer
   - **Intel Mac:** the `x86_64` `.pkg` installer

   If you are unsure which chip your Mac has, go to **Apple menu → About This
   Mac**. It will say either "Apple M..." or "Intel".

2. Open the downloaded `.pkg` file and follow the installer steps. Accept the
   defaults.

3. Open **Terminal** (search for it in Spotlight with ⌘ Space). You should see
   `(base)` at the start of your prompt. If you do not, run:

   ```bash
   conda init zsh
   ```

   Then close and reopen Terminal.

### Linux

Open a terminal and run:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

Accept the licence, use the default install location, and say **yes** when
asked to initialise conda. Close and reopen the terminal. You should see
`(base)` in your prompt.

### Verify the installation

In your terminal (Anaconda Prompt on Windows), run:

```bash
conda --version
python --version
```

Both should print version numbers. If either command is not found, the
installation did not complete correctly — re-run the installer.

---

## Part 2 — Create a project environment

A conda **environment** is an isolated Python installation with its own set of
packages. Creating a dedicated environment for this project means its packages
will never conflict with other Python work you do.

### Step 2.1 — Create the environment

In your terminal, run:

```bash
conda create -n stm-analysis python=3.11
```

This creates a new environment called `stm-analysis` running Python 3.11.
Type `y` and press Enter when prompted.

### Step 2.2 — Activate the environment

```bash
conda activate stm-analysis
```

Your prompt will change from `(base)` to `(stm-analysis)`:

```
(stm-analysis) C:\Users\YourName>
```

> **Important:** You must activate the environment every time you open a new
> terminal. If you forget, packages you install will go into `(base)` instead,
> and your project code will not find them.

### Step 2.3 — Install the project packages

With the `stm-analysis` environment active, run:

```bash
conda install -c conda-forge numpy scipy matplotlib scikit-image networkx pandas jupyter ipykernel
```

This installs:

| Package | Purpose |
|---------|---------|
| `numpy` | Fast array computation |
| `scipy` | Scientific algorithms (KDTree, statistics) |
| `matplotlib` | Plotting |
| `scikit-image` | Image processing |
| `networkx` | Graph algorithms |
| `pandas` | Tabular data and CSV export |
| `jupyter` | Jupyter Notebook and JupyterLab |
| `ipykernel` | Connects the environment to VS Code's Jupyter |

Type `y` when prompted. This will take a few minutes.

### Step 2.4 — Register the environment as a Jupyter kernel

This step makes the `stm-analysis` environment available when you open a
Jupyter Notebook, both in the browser and in VS Code.

```bash
python -m ipykernel install --user --name stm-analysis --display-name "Python (stm-analysis)"
```

You can verify it was registered with:

```bash
jupyter kernelspec list
```

You should see `stm-analysis` in the list.

### Step 2.5 — Verify the installation

Still in the activated environment, run:

```bash
python -c "import numpy, scipy, matplotlib, skimage, networkx, pandas; print('All packages OK')"
```

If this prints `All packages OK`, your environment is correctly set up.

---

## Part 3 — Install and configure VS Code

VS Code is a free, powerful code editor made by Microsoft. It has excellent
support for Python and Jupyter Notebooks through extensions.

### Step 3.1 — Install VS Code

Download and install VS Code from:
[https://code.visualstudio.com/](https://code.visualstudio.com/)

Accept all defaults during installation. On Windows, check both
"Add to PATH" options when they appear — this lets you open VS Code from
the terminal by typing `code .`.

### Step 3.2 — Install the Python extension

1. Open VS Code.
2. Click the **Extensions** icon in the left sidebar (it looks like four
   squares, or press `Ctrl+Shift+X` / `⌘+Shift+X`).
3. Search for **Python** and install the extension published by **Microsoft**.
4. Search for **Jupyter** and install the extension published by **Microsoft**.

These two extensions give VS Code full Python language support, linting,
autocomplete, and the ability to run Jupyter Notebooks directly in the editor.

### Step 3.3 — Select the project interpreter

VS Code needs to know which Python environment to use.

1. Open the **Command Palette** with `Ctrl+Shift+P` (Windows/Linux) or
   `⌘+Shift+P` (macOS).
2. Type `Python: Select Interpreter` and press Enter.
3. You should see a list of available environments. Select the one labelled
   **Python (stm-analysis)** or showing a path containing `stm-analysis`.

If the environment does not appear, click **Enter interpreter path** and
navigate to the Python executable manually:
- **Windows:** `C:\Users\YourName\miniconda3\envs\stm-analysis\python.exe`
- **macOS/Linux:** `~/miniconda3/envs/stm-analysis/bin/python`

You can verify the correct interpreter is active by looking at the bottom-left
status bar in VS Code — it should show the environment name.

### Step 3.4 — Recommended VS Code settings

These settings make VS Code more useful for scientific Python work. Open
Settings with `Ctrl+,` (or `⌘+,`) and search for each setting by name, or
add them directly to your `settings.json` (`Ctrl+Shift+P` → "Open User
Settings (JSON)"):

```json
{
    "python.defaultInterpreterPath": "~/miniconda3/envs/stm-analysis/bin/python",
    "editor.formatOnSave": true,
    "editor.rulers": [79],
    "notebook.lineNumbers": "on",
    "jupyter.askForKernelRestart": false
}
```

**What these do:**

| Setting | Effect |
|---------|--------|
| `formatOnSave` | Auto-formats your Python code when you save |
| `rulers` | Shows a vertical line at 79 characters (PEP 8 line length guide) |
| `notebook.lineNumbers` | Shows line numbers in Jupyter cells |
| `askForKernelRestart` | Skips the confirmation dialog when restarting a kernel |

### Step 3.5 — Useful VS Code keyboard shortcuts

Learning these will save significant time.

| Shortcut (Win/Linux) | Shortcut (macOS) | Action |
|----------------------|-----------------|--------|
| `Ctrl+Shift+P` | `⌘+Shift+P` | Open Command Palette |
| `Ctrl+,` | `⌘+,` | Open Settings |
| `Ctrl+`` ` | `Ctrl+`` ` | Open integrated terminal |
| `F5` | `F5` | Run Python file |
| `Shift+Enter` | `Shift+Enter` | Run notebook cell and advance |
| `Ctrl+Enter` | `Ctrl+Enter` | Run notebook cell in place |
| `Ctrl+Shift+\` | `⌘+Shift+\` | Jump to matching bracket |
| `Alt+Up/Down` | `Option+Up/Down` | Move line up or down |
| `Ctrl+/` | `⌘+/` | Toggle comment on selected lines |
| `F2` | `F2` | Rename a variable everywhere in the file |

---

## Part 4 — Set up the project folder

### Step 4.1 — Clone the project repository

Clone the repository. You can do this with the commands below, or if you `GitHub Desktop`
on the GitHub page https://github.com/GallagherSurfaceLab/summer_26.git click the gree
code button and navigate to `Open with GitHub Desktop`, this will prompt you to save the
repository locally and will initialize everything for Git.

```bash
cd ~                          # go to the directory you want to store your project
git clone https://github.com/GallagherSurfaceLab/summer_26.git
cd summer_26
```

### Step 4.2 — Open the project in VS Code

From the terminal, inside the project folder, run:

```bash
code .
```

This opens VS Code with the current folder as the workspace. You should see
the project files in the Explorer panel on the left.

> **Tip:** Always open VS Code from inside your project folder using `code .`
> rather than opening it from the Start menu or Dock. This ensures VS Code
> knows which folder you are working in and can find your files correctly.
> You can also open the project by right clicking the folder and going to
> `Open with Code`  

---

## Part 5 — Working with Jupyter Notebooks in VS Code

VS Code can open and run `.ipynb` notebook files directly, without launching a
separate browser window. This is often more convenient than the classic Jupyter
interface.

### Step 5.1 — Open a notebook

In the VS Code Explorer panel, click on `STM_voronoi.ipynb`. It will open in
the notebook editor.

### Step 5.2 — Select the kernel

At the top right of the notebook editor, you will see a button showing the
current kernel (it may say "Select Kernel" if none is chosen). Click it and
select **Python (stm-analysis)** from the list.

If the environment does not appear, make sure you completed Step 2.4
(registering the kernel) and try restarting VS Code.

### Step 5.3 — Run cells

- `Shift+Enter` — run the current cell and move to the next one
- `Ctrl+Enter` — run the current cell and stay on it
- The play button (▶) at the top runs all cells in order

### Step 5.4 — Restart the kernel

If your notebook gets into a broken state (e.g. you redefined a variable in an
unexpected order), restart the kernel and re-run everything from the top:

- Click the restart button (⟳) in the notebook toolbar, or
- Open the Command Palette and type **Jupyter: Restart Kernel**

> **Good habit:** Before sharing a notebook or considering a task done, always
> do **Restart Kernel and Run All Cells** to confirm the notebook runs cleanly
> from top to bottom without errors.

---

## Part 6 — Daily workflow

This is the sequence you should follow at the start of every work session.

### In the terminal

```bash
# 1. Activate the project environment
conda activate stm-analysis

# 2. Navigate to the project folder
cd ~/stm-project

# 3. Pull the latest code from GitHub
git pull

# 4. Open VS Code
code .
```

### In VS Code

1. Open the notebook or `.py` file you are working on.
2. Confirm the kernel/interpreter shows **Python (stm-analysis)** in the
   status bar.
3. Work through your task, committing and pushing regularly using GitHub Desktop

---

## Part 7 — Managing packages

### Installing a new package

Always activate your environment first, then install:

```bash
conda activate stm-analysis
conda install -c conda-forge package-name
```

Prefer `conda install` over `pip install` for scientific packages — conda
handles binary dependencies (like compiled C extensions in NumPy and SciPy)
more reliably. Use `pip install` only for packages not available on conda-forge.

### Saving your environment

To save a record of all installed packages (useful for sharing with your
supervisor or reproducing the environment on another computer):

```bash
conda env export > environment.yml
```

Add this file to your Git repository:

```bash
git add environment.yml
git commit -m "Add conda environment file"
```

### Recreating an environment from the file

On a new computer, or to restore after something goes wrong:

```bash
conda env create -f environment.yml
conda activate stm-analysis
```

---

## Part 8 — Troubleshooting

### "conda: command not found" or "conda is not recognised"

- **Windows:** Make sure you are using **Anaconda Prompt**, not the regular
  Command Prompt or PowerShell.
- **macOS/Linux:** Run `conda init zsh` (or `conda init bash`) and reopen
  the terminal.

### VS Code is not finding my environment

1. Make sure you activated the environment in the terminal before opening
   VS Code (`conda activate stm-analysis`).
2. In VS Code, open the Command Palette and run `Python: Select Interpreter`.
3. If it still does not appear, provide the full path to the Python executable:
   - Windows: `C:\Users\YourName\miniconda3\envs\stm-analysis\python.exe`
   - macOS/Linux: `~/miniconda3/envs/stm-analysis/bin/python`

### The notebook kernel keeps crashing

This usually means a cell is running out of memory or hitting an error. Try:

1. Restart the kernel (`Ctrl+Shift+P` → "Jupyter: Restart Kernel").
2. Run cells one at a time to find the problem cell.
3. Check that your image file exists and the path is correct.

### "ModuleNotFoundError: No module named 'skimage'"

This means the notebook is not using the `stm-analysis` environment. Check:

1. The kernel shown at the top right of the notebook — it should say
   "Python (stm-analysis)".
2. Click it and select the correct kernel.
3. Restart the kernel after switching.

### A conda install takes a very long time or fails

Try using the `mamba` solver, which is faster:

```bash
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

Then re-run your original install command.

---

## Quick reference card

```
# Environment
conda create -n stm-analysis python=3.11     create environment
conda activate stm-analysis                  activate environment
conda deactivate                             leave environment
conda env list                               list all environments

# Packages
conda install -c conda-forge package-name    install a package
conda list                                   list installed packages
conda env export > environment.yml           save environment to file
conda env create -f environment.yml          recreate from file

# Jupyter
jupyter notebook                             launch in browser
jupyter kernelspec list                      list registered kernels

# VS Code
code .                                       open current folder in VS Code

# Daily Git workflow
git pull                                     get latest changes
git status                                   see what has changed
git add .                                    stage all changes
git commit -m "message"                      save a snapshot
git push                                     upload to GitHub
```
 

 

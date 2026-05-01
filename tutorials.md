#### Step 1.3 — Install Git
 
Git is version control software — it tracks every change you make to your code, lets you go back to previous versions, and enables collaboration.
 
- **Windows:** Download Git for Windows from [https://git-scm.com/download/win](https://git-scm.com/download/win). Accept the defaults during installation. This also installs **Git Bash**, a terminal you will use for Git commands.
- **macOS:** Run `git --version` in Terminal. If Git is not installed, macOS will prompt you to install the Xcode Command Line Tools, which includes Git.
- **Linux:** Run `sudo apt install git` (Ubuntu/Debian) or `sudo dnf install git` (Fedora).
After installation, open a terminal and configure Git with your name and email (these appear in your commit history):
 
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
 
**Learning task:** Run `git --version` and confirm it prints a version number.
 
#### Step 1.4 — Create a GitHub account
 
GitHub is a website that hosts Git repositories online. It lets you back up your code, share it with your supervisor, and collaborate.
 
- Sign up at [https://github.com](https://github.com). Use your university email address.
- Apply for the **GitHub Student Developer Pack** at [https://education.github.com/pack](https://education.github.com/pack) — this gives you free access to GitHub Pro and other tools while you are a student.
---
 
### Part 2 — Learning Python for scientific computing
 
Work through these in order. Each should take 1–3 hours. You do not need to finish all of them before starting the project tasks — complete Steps 2.1–2.3 first, then return to the rest as needed.
 
#### Step 2.1 — Python basics (if new to Python)
 
**Resource:** The official Python tutorial, sections 3–5: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
 
**Topics to cover:**
- Variables, types (int, float, str, list)
- `if`, `for`, and `while` statements
- Defining functions with `def`
- Importing modules with `import`
**Learning task:** Write a function that takes a list of numbers and returns the mean and standard deviation without using NumPy (use plain Python loops). Then verify your answer matches `np.mean()` and `np.std(ddof=1)`.
 
#### Step 2.2 — NumPy fundamentals
 
NumPy is the foundation of scientific Python. Almost all array operations in the STM code use it.
 
**Resource:** NumPy quickstart: [https://numpy.org/doc/stable/user/quickstart.html](https://numpy.org/doc/stable/user/quickstart.html)
 
**Topics to cover:**
- Creating arrays: `np.array()`, `np.zeros()`, `np.ones()`, `np.linspace()`, `np.arange()`
- Array indexing and slicing: `arr[0]`, `arr[1:5]`, `arr[:, 0]`
- Vectorized operations: `arr * 2`, `arr + other_arr`
- Useful functions: `np.mean()`, `np.std()`, `np.sum()`, `np.sqrt()`, `np.where()`
- Boolean masking: `arr[arr > 0]`
**Learning task:** Create a 2D array of shape (100, 100) filled with random values, then compute the mean of all values above 0.5 using boolean masking (without any loops).
 
#### Step 2.3 — Matplotlib for plotting
 
**Resource:** Matplotlib getting started: [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
 
**Topics to cover:**
- `plt.plot()`, `plt.scatter()`, `plt.hist()`, `plt.imshow()`
- Adding labels: `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.legend()`
- Subplots: `fig, axes = plt.subplots(1, 2)`
- Saving figures: `plt.savefig('output.png', dpi=150)`
**Learning task:** Plot a sine wave and a cosine wave on the same figure with a legend, axis labels, and a title. Save it to a PNG file.
 
#### Step 2.4 — Writing and calling functions
 
**Resource:** Real Python guide to functions: [https://realpython.com/defining-your-own-python-function/](https://realpython.com/defining-your-own-python-function/)
 
**Topics to cover:**
- Positional and keyword arguments
- Default argument values
- Returning multiple values with tuples
- Writing docstrings (what they are and why they matter)
**Learning task:** Write a function `summarize(data, label="data")` that takes a NumPy array and prints the min, max, mean, and standard deviation with the given label. Add a NumPy-style docstring.
 
#### Step 2.5 — pandas for tabular data
 
Needed for Task 5 (batch processing).
 
**Resource:** pandas getting started: [https://pandas.pydata.org/docs/getting_started/10min.html](https://pandas.pydata.org/docs/getting_started/10min.html)
 
**Topics to cover:**
- Creating a DataFrame from a list of dicts
- Accessing columns: `df['column_name']`
- Computing column statistics: `df.mean()`, `df.std()`
- Saving to CSV: `df.to_csv('file.csv', index=False)`
- Reading from CSV: `pd.read_csv('file.csv')`
**Learning task:** Create a DataFrame with columns `['filename', 'mean_edge', 'std_edge', 'defect_ratio']` and three made-up rows, then save it to CSV and read it back.
 
---
 
### Part 3 — Learning Git and GitHub
 
Work through these in order. The first two are the most important and cover everything you need for day-to-day use on this project.
 
#### Step 3.1 — Core Git concepts
 
Before using Git commands, understand what they do conceptually.
 
**Resource:** Git handbook (GitHub): [https://guides.github.com/introduction/git-handbook/](https://guides.github.com/introduction/git-handbook/)
 
**Key concepts to understand:**
- **Repository (repo):** a folder that Git is tracking
- **Commit:** a saved snapshot of your code at a point in time
- **Branch:** a parallel version of your code (you will mostly work on `main`)
- **Working directory vs staging area vs committed history:** the three states a file can be in
**Learning task:** Read the handbook and write a one-paragraph plain-English explanation of what a commit is and why you would make one. (No code needed — this is a reading comprehension exercise.)
 
#### Step 3.2 — Basic Git workflow
 
These are the commands you will use every day. Practice them until they feel natural.
 
**Resource:** Git basics chapter from *Pro Git* (free online): [https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository](https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository)
 
**Commands to learn:**
 
```bash
git init                   # initialise a new repo in the current folder
git status                 # see what has changed
git add filename.py        # stage a file for the next commit
git add .                  # stage all changed files
git commit -m "message"    # save a snapshot with a description
git log                    # see the commit history
git diff                   # see what changed since the last commit
```
 
**Learning task:**
 
1. Create a new folder called `practice_repo`.
2. Run `git init` inside it.
3. Create a file `hello.py` containing `print("Hello, Git!")`.
4. Stage and commit it with the message `"Add hello.py"`.
5. Edit the file to print a different message.
6. Run `git diff` to see the change, then stage and commit again.
7. Run `git log` and confirm two commits appear.
#### Step 3.3 — Working with GitHub
 
**Resource:** GitHub quickstart: [https://docs.github.com/en/get-started/quickstart/create-a-repo](https://docs.github.com/en/get-started/quickstart/create-a-repo)
 
**Commands to learn:**
 
```bash
git remote add origin https://github.com/username/repo.git   # link local repo to GitHub
git push -u origin main    # upload commits to GitHub (first time)
git push                   # upload commits to GitHub (after first time)
git pull                   # download any changes from GitHub
git clone https://github.com/username/repo.git   # download a repo from GitHub
```
 
**Learning task:**
 
1. Create a new repository on GitHub called `stm-practice` (set it to Private).
2. Link your local `practice_repo` folder to it using `git remote add origin ...`.
3. Push your commits to GitHub.
4. Open GitHub in a browser and verify your files and commit history appear there.
#### Step 3.4 — Branching and merging (intermediate)
 
Branching lets you develop a new feature or fix without disturbing your working code on `main`. This is good practice for any non-trivial change.
 
**Resource:** Learn Git Branching (interactive visual tutorial): [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
 
**Commands to learn:**
 
```bash
git branch feature/vectorize-statistics   # create a new branch
git checkout feature/vectorize-statistics # switch to it
git checkout -b feature/name              # create and switch in one step
git merge feature/name                    # merge changes back into main
git branch -d feature/name               # delete a branch after merging
```
 
**Learning task:** Complete the first three levels of the "Introduction Sequence" on [https://learngitbranching.js.org/](https://learngitbranching.js.org/). This interactive tool shows you exactly what branching looks like visually.
 
#### Step 3.5 — Good commit habits
 
Good commit messages make your project history readable and make it easy to find when a bug was introduced.
 
**Rules for good commit messages:**
 
1. Use the imperative mood: "Fix area calculation bug" not "Fixed area calculation bug" or "Fixes bug"
2. Keep the first line under 72 characters
3. Make one commit per logical change — do not bundle five unrelated fixes into one commit
4. Reference the task number in the message: `"Fix area calculation bug (Task 1)"`
**Examples of good commit messages for this project:**
 
```
Fix area calculation bug in img_file.load() (Task 1)
Add img_as_ubyte() conversion to suppress UserWarning (Task 2)
Vectorize statistics() edge length computation (Task 3)
Add plot_voronoi() helper function (Task 4)
```
 
**Recommended branch naming convention for this project:**
 
```
feature/task-01-area-bug-fix
feature/task-03-vectorize-statistics
feature/task-07-synthetic-lattice-test
```
 
**Learning task:** For your next project task, create a branch using this naming convention, complete the task, commit with a message following the rules above, and push the branch to GitHub.
 
---
 
### Part 4 — Recommended workflow for each task
 
Use this checklist for every task on the Kanban board:
 
```
[ ] Read the task card fully before writing any code
[ ] Pull the latest code from GitHub: git pull
[ ] Create a new branch: git checkout -b feature/task-XX-short-description
[ ] Read the relevant functions in stm_voronoi_mst.py before editing
[ ] Make your changes in small steps, testing as you go
[ ] Commit regularly (after each logical sub-step, not just at the end)
[ ] Write or update a docstring for any function you modify
[ ] Test your changes on the example notebook before considering the task done
[ ] Push your branch to GitHub: git push -u origin feature/task-XX-...
[ ] Move the card to "Done" on the Kanban board
```
 
---
 
### Quick reference — commands you will use every day
 
```bash
# Start of each work session
git pull                              # get latest changes
 
# During work
git status                            # check what has changed
git add filename.py                   # stage a specific file
git add .                             # stage everything
git commit -m "Descriptive message"   # save a snapshot
 
# End of each work session
git push                              # upload to GitHub
 
# Starting a new task
git checkout main                     # go back to main branch
git pull                              # make sure it is up to date
git checkout -b feature/task-XX-name  # create branch for new task
```
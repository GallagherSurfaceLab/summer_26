## Learning Python for scientific computing
 
Work through the Python tutorials below and the [GitHub](#learning-git-and-github) section at the end. Additoinal resources are below. You do not need to finish all of them before starting the project tasks — complete the tutorials, then return to the rest as needed.

## Python Tutorials

The two tutorials below are GitHub repositories. You can naviage to their GitHub site, clone the repositories (Green `< > Code` button) and then work through each of the notebooks.

- [Goodard Heliophysics Boot Camp](https://github.com/helio670/bootcamp)
- [Goddar Heliophysics Data Science](https://github.com/helio670/datascience)

There are a number of other tutorials that may be of use
- [Scientific Python Lectures](https://lectures.scientific-python.org/)
- [Kaggle intro to Python](https://www.kaggle.com/learn/python)
- [Intro To Python](https://www.datacamp.com/courses/intro-to-python-for-data-science)


 
#### Python basics (if new to Python)
 
**Resource:** The official Python tutorial, sections 3–5: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/)
 
**Topics to cover:**
- Variables, types (int, float, str, list)
- `if`, `for`, and `while` statements
- Defining functions with `def`
- Importing modules with `import`
**Learning task:** Write a function that takes a list of numbers and returns the mean and standard deviation without using NumPy (use plain Python loops). Then verify your answer matches `np.mean()` and `np.std(ddof=1)`.
 
#### NumPy fundamentals
 
NumPy is the foundation of scientific Python. Almost all array operations in the STM code use it.
 
**Resource:** NumPy quickstart: [https://numpy.org/doc/stable/user/quickstart.html](https://numpy.org/doc/stable/user/quickstart.html)
 
**Topics to cover:**
- Creating arrays: `np.array()`, `np.zeros()`, `np.ones()`, `np.linspace()`, `np.arange()`
- Array indexing and slicing: `arr[0]`, `arr[1:5]`, `arr[:, 0]`
- Vectorized operations: `arr * 2`, `arr + other_arr`
- Useful functions: `np.mean()`, `np.std()`, `np.sum()`, `np.sqrt()`, `np.where()`
- Boolean masking: `arr[arr > 0]`
**Learning task:** Create a 2D array of shape (100, 100) filled with random values, then compute the mean of all values above 0.5 using boolean masking (without any loops).
 
#### Matplotlib for plotting
 
**Resource:** Matplotlib getting started: [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
 
**Topics to cover:**
- `plt.plot()`, `plt.scatter()`, `plt.hist()`, `plt.imshow()`
- Adding labels: `plt.xlabel()`, `plt.ylabel()`, `plt.title()`, `plt.legend()`
- Subplots: `fig, axes = plt.subplots(1, 2)`
- Saving figures: `plt.savefig('output.png', dpi=150)`
**Learning task:** Plot a sine wave and a cosine wave on the same figure with a legend, axis labels, and a title. Save it to a PNG file.
 
#### Writing and calling functions
 
**Resource:** Real Python guide to functions: [https://realpython.com/defining-your-own-python-function/](https://realpython.com/defining-your-own-python-function/)
 
**Topics to cover:**
- Positional and keyword arguments
- Default argument values
- Returning multiple values with tuples
- Writing docstrings (what they are and why they matter)
**Learning task:** Write a function `summarize(data, label="data")` that takes a NumPy array and prints the min, max, mean, and standard deviation with the given label. Add a NumPy-style docstring.
 
#### pandas for tabular data
 
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
 
### Learning Git and GitHub
 
Work through these in order. The first two are the most important and cover everything you need for day-to-day use on this project.
 
#### Core Git concepts
 
Before using Git commands, understand what they do conceptually.
 
**Resource:** Git handbook (GitHub): [https://guides.github.com/introduction/git-handbook/](https://guides.github.com/introduction/git-handbook/)
 
**Key concepts to understand:**
- **Repository (repo):** a folder that Git is tracking
- **Commit:** a saved snapshot of your code at a point in time
- **Branch:** a parallel version of your code (you will mostly work on `main`)
- **Working directory vs staging area vs committed history:** the three states a file can be in
**Learning task:** Read the handbook and write a one-paragraph plain-English explanation of what a commit is and why you would make one. (No code needed — this is a reading comprehension exercise.)

#### Git Tutorials

- [Git, GitHub, & GitHub Desktop for beginners](https://www.youtube.com/watch?v=8Dd7KRpKeaE)
- [git - the simple guide](https://rogerdudler.github.io/git-guide/)
- [GitHub Docs - Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world)
- [Git and GitHub for Beginners - Crash Course](https://www.youtube.com/watch?v=RGOj5yH7evk)
 
#### Basic Git workflow
 
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
 
#### Good commit habits
 
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
#!/usr/bin/env python3
"""Builds the Manta Institute static site into ./site"""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
APPLY = "https://forms.gle/bUK9oC2Zib9sQvzj8"
EMAIL = "info@mantainstitute.org"
YOUTUBE = "https://www.youtube.com/@MantaInstituteforMathematics"
YT_ICON = '<svg class="yt-icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg>'

NAV = [("index.html", "Home"), ("about.html", "About"), ("courses.html", "Courses"),
       ("journey.html", "The Journey")]

def page(fname, title, desc, body, head_extra=""):
    menu = "".join(
        f'<li><a href="/{"" if f=="index.html" else f[:-5]}"{" aria-current=page" if f==fname else ""}>{n}</a></li>'
        for f, n in NAV)
    full_title = "Manta Institute for Mathematics" if fname == "index.html" else f"{title} — Manta Institute for Mathematics"
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://www.mantainstitute.org/img/og.jpg">
<meta property="og:type" content="website">
<link rel="icon" href="/favicon.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&family=Source+Sans+3:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/style.css">
{head_extra}
</head>
<body>
<header class="site-header">
  <nav class="nav" aria-label="Main">
    <a class="brand" href="/">
      <img src="/img/manta-mark.png" alt="" width="52" height="52">
      <span><b>Manta Institute for Mathematics</b><small>Prove. Connect. Protect.</small></span>
    </a>
    <button class="menu-toggle" aria-expanded="false" aria-controls="menu">Menu</button>
    <ul class="menu" id="menu">{menu}<li><a class="yt-nav" href="{YOUTUBE}" target="_blank" rel="noopener">{YT_ICON}<span>YouTube</span></a></li><li><a class="cta" href="{APPLY}">Apply</a></li></ul>
  </nav>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="cols">
    <div>
      <p class="brandline">Manta Institute for Mathematics</p>
      <p>Proving theorems, building minds — beginning in Sri Lanka and extending globally. Free of charge to students.</p>
    </div>
    <div>
      <h4>Explore</h4>
      <ul>
        <li><a href="/about">About</a></li>
        <li><a href="/courses">Courses</a></li>
        <li><a href="/journey">The Journey</a></li>
      </ul>
    </div>
    <div>
      <h4>Contact</h4>
      <ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{APPLY}">Apply to the Prep Program</a></li>
        <li><a class="yt-foot" href="{YOUTUBE}" target="_blank" rel="noopener">{YT_ICON} YouTube: lectures &amp; videos</a></li>
      </ul>
    </div>
  </div>
  <p class="fine">© 2026 Manta Institute for Mathematics</p>
</footer>
<script>
const t=document.querySelector('.menu-toggle'),m=document.getElementById('menu');
t.addEventListener('click',()=>{{const o=m.classList.toggle('open');t.setAttribute('aria-expanded',o)}});
</script>
</body>
</html>
"""
    with open(os.path.join(OUT, fname), "w") as f:
        f.write(html)

# ---------------------------------------------------------------- HOME
home = f"""
<section class="hero" style="background-image:url('/img/notes-1.jpg')">
  <div class="inner">
    <h1>Proving Theorems,<br>Building Minds</h1>
    <p>The Manta Institute for Mathematics is dedicated to nurturing the next generation of pure mathematicians — beginning in Sri Lanka and extending globally. We offer deep mentorship, rigorous training, and a life-long intellectual community.</p>
    <p><a class="btn" href="/about">Our Mission</a> <a class="btn ghost" href="/courses">See the Courses</a></p>
  </div>
</section>

<section class="band" style="background-image:url('/img/notes-2.jpg')">
  <div class="inner">
    <h2>The Prep Program is Open</h2>
    <p>For students with discipline, hunger, and heart — the Manta Prep Program offers an intensive path into modern mathematics. No tuition. No fluff. Just you, your ideas, and the mentors who will help sharpen them.</p>
    <p><a class="btn" href="{APPLY}">Apply Now</a> <a class="btn ghost" href="/courses">Courses &amp; Materials</a></p>
  </div>
</section>

<section class="band yt-band">
  <div class="inner">
    <h2>Watch the Lectures on YouTube</h2>
    <p>Full course lectures — Foundations of Mathematics, Linear Algebra, Statistics and more — are free on the Manta Institute YouTube channel. Start watching today, no application needed.</p>
    <div class="video"><iframe src="https://www.youtube-nocookie.com/embed/HKouQj8MpVQ" title="Join Manta Institute for Mathematics After A/L" loading="lazy" allow="accelerometer; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
    <p><a class="btn yt" href="{YOUTUBE}" target="_blank" rel="noopener">{YT_ICON} Visit our YouTube Channel</a> <a class="btn ghost" href="/courses">Course Playlists</a></p>
  </div>
</section>

<section class="band plain">
  <div class="inner">
    <h2>Our First Generation is Rising</h2>
    <p>Young mathematicians from Sri Lanka are now ready to enter elite programs across the world — trained with care, supported with integrity, and driven by ideas that matter. This fall, thirteen students mentored through Manta are heading to programs like <em>Math in Moscow</em>.</p>
  </div>
</section>

<section class="band" style="background-image:url('/img/notes-4.jpg')">
  <div class="inner">
    <h2>100 is the Goal</h2>
    <p class="squares">1 · 4 · 9 <span>· 16 · 25 · 36 · 49 · 64 · 81 · 100</span></p>
    <p>We’ve taken the first three steps — seven to go.</p>
    <p>Our long-term target is <strong>100 deeply mentored students per year</strong>. That is enough to match the per-capita output of countries like Hungary, Israel, and France, to create a dense network of future researchers, mentors, and teachers — and to change the mathematical landscape of a country in a single generation.</p>
    <p>Whether you mentor, donate, or simply believe in minds worth cultivating, your support helps uncover and elevate mathematical talent where it’s most needed. Manta is a movement, and you are invited.</p>
    <p><a class="btn ghost" href="/about#why-100">Why 100?</a></p>
  </div>
</section>

<section class="band" style="background-image:url('/img/notes-5.jpg')">
  <div class="inner">
    <h2>The Founder’s Journey</h2>
    <p>Dr. Prabath Silva rose from Sri Lanka to the top of global mathematics — earning his place at elite academic institutions abroad.</p>
    <p>He returned home not in triumph, but in service. He chose to leave the university system — disillusioned by its inertia — and began again, from scratch: mentoring a few kids in a beach house, teaching mathematics, dreaming freely, and building the habits that change lives.</p>
    <p>One brick at a time, he laid the foundation for a legacy of mentorship. Now, with a generation rising and a path mapped clearly, the mission needs a team. Not thousands. Just the right few.</p>
    <p><a class="btn" href="/journey">The Long Journey Ahead</a> <a class="btn ghost" href="/about#founder">About the Founder</a></p>
  </div>
</section>
"""
page("index.html", "Home", "Manta Institute for Mathematics — deep mentorship and rigorous training for the next generation of pure mathematicians, beginning in Sri Lanka. Free for students.", home)

# ---------------------------------------------------------------- ABOUT
about = f"""
<div class="read">
<header class="page-head">
  <p class="kicker">About</p>
  <h1>Founder’s Vision</h1>
  <p class="lede">We are building this for Sri Lanka’s future in pure mathematics — and for those of you who still believe, like I do, that one day a Sri Lankan will win the Abel Prize.</p>
</header>

<p>The <strong>Manta Institute for Mathematics</strong> is dedicated to training the next generation of theorem-proving mathematicians. We offer deep mentorship, advanced seminars, and global research access — <strong>free of charge to students</strong>, just like the free education system in Sri Lanka.</p>
<p>Not a school, not a prep center, and definitely not an easy path to immigration. This is a launchpad for those rare minds who want to prove a new theorem.</p>
<p>Mathematics is more than exams or jobs. It’s the art of discovering new structures — and proving theorems about those structures. Some of those structures appear in nature and can be used as a language to describe nature; some exist only in our imaginations. Both are equally important.</p>
<p>The world’s great research mathematicians are not born with titles. They train for decades, often with a mentor alongside them, working toward breakthroughs that can take 20–30 years to complete. This is the quiet path of greatness.</p>
<p>I walked that path myself — from a Sri Lankan school to Caltech, a PhD in Harmonic Analysis, a postdoc in Spectral Function Theory, and years of research in the U.S. At every stage I saw how invisible this path is to students back home — and how many give up, not because they aren’t good enough, but because they were never shown the way.</p>
<p>Our aim is to cultivate researchers: people who want to prove something original. We also recognize that some Fellows will move into high-demand quantitative industries — AI, finance, and more — and we create exit paths for those too.</p>

<h2>Our Mission</h2>
<ol class="steps">
  <li><b>Preparation Program</b>We begin with ~200 high school and early university students in the <strong>Manta Fellowship Preparation Program</strong>, taught the first semester of university mathematics — the material Caltech math majors study.</li>
  <li><b>Manta Fellows</b>After one semester, ~100 students are selected as <strong>Manta Fellows</strong> and taught three more semesters alongside their university studies in Sri Lanka.</li>
  <li><b>Global programs</b>Fellows are sent to programs like <em>Math in Moscow</em> to study graduate-level mathematics. Thirteen students — most of whom I mentored in Sri Lanka — are going this fall.</li>
  <li><b>Research careers</b>The goal: launch at least 50 into top PhD programs in mathematics or adjacent fields — theoretical physics, mathematical finance, AI, computational biology.</li>
</ol>
<p>This will always be free for students. It supports long-term research, not short-term exams, and it will build a new generation of mentors and thinkers.</p>

<h3>Future plans: reaching younger students</h3>
<p>The Grade 5 scholarship exam gathers talented children from every corner of the country. I plan to keep them mathematically occupied — especially children in hostels — with a time-tested fast track for talented students from grade 6 up, using the classic British texts and taking time to dive deep.</p>

<h2 id="why-100">Why 100 Is Enough</h2>
<p>We are building toward <strong>100 deeply mentored students per year</strong> with the curiosity and discipline to explore serious mathematics — not just test performance, but proof, structure, and original thought. 100 per year is enough to:</p>
<ul>
  <li>Match or exceed the per-capita output of world-leading countries like Hungary, Israel, and France.</li>
  <li>Create a dense network of future researchers, mentors, and teachers.</li>
  <li>Change the mathematical landscape of a country over a single generation.</li>
</ul>
<p>We are not trying to scale endlessly. We are trying to build depth, continuity, and legacy.</p>
<p><strong>Some will drift — as they should.</strong> Some will go on to theoretical physics, AI, quantitative social science, or philosophy. Some will become educators, collaborators, or seminar organizers. Some will become true mathematicians — climbing the mountain and guiding others upward.</p>
<p><strong>Mathematics is an individual sport.</strong> Just like cricket, Sri Lanka has made a global impact through a few dedicated individuals. It takes one genius with structure, one mentor with time, one program with faith. You don’t need a million players — you need the right pipeline, ethos, and early-stage care.</p>
<div class="note"><strong>Ten years of 100 students.</strong> Even if 30 shift fields, 30 become researchers, 30 return to teach and mentor, and 10 push into the frontier — you will have built <strong>Sri Lanka’s first complete mathematical generation</strong>, capable of sustaining itself and joining the global community on equal terms.</div>

<h2 id="founder">About the Founder</h2>
<p>Dr. Prabath Silva is a mathematician, mentor, and founder of the Manta Institute for Mathematics. Born and raised in Sri Lanka, he followed a long and winding path — from a small island to some of the most prestigious institutions in the United States — only to return home and begin again.</p>
<p>After establishing himself among world-class mathematicians, he came home with a clear intention: to give back. He joined the university system, but soon found that a small beach house by the sea offered a better environment for the kind of mentorship he valued most. There, outside the formal system, a handful of students became many. Some now walk the halls of elite PhD programs in the U.S.; others are preparing to follow.</p>
<p>Today Dr. Silva lives in the U.S. again, but the mission has only grown. The Manta Institute is his legacy project — a place for long-term mentorship, cultural transformation, and rigorous training in pure mathematics. Not an institution in the traditional sense, but a <strong>home for minds worth building</strong>.</p>
<blockquote>“When you come home and choose to leave again, it’s no longer about guiding a few — it’s about building for many, across generations.”</blockquote>
<p>At the heart of the Institute is a belief: that <strong>one good teacher</strong>, over time, can change the fate of a student — and that <strong>a culture of thinkers</strong>, given space and support, can begin to shape the world. Like its namesake, the manta ray — silent, graceful, and powerful — the Institute carries its students forward, steadily, across oceans of thought.</p>
<blockquote>“To those who feel called to think deeply: you don’t have to go it alone. You don’t have to chase prestige. If you have the discipline, the hunger, and the heart — there is a place for you here. I built the Manta Institute for you.”<cite>— Dr. Prabath Silva</cite></blockquote>
<p><a class="btn" href="/journey">Read: The Long Journey Ahead</a></p>
</div>
"""
page("about.html", "About", "The vision and mission of the Manta Institute for Mathematics, and its founder Dr. Prabath Silva.", about)

# ---------------------------------------------------------------- COURSES
yt = lambda u, t: f'<a class="btn yt" href="{u}" target="_blank" rel="noopener">{YT_ICON} {t}</a>'
courses = f"""
<div class="wrap">
<header class="page-head">
  <p class="kicker">Courses</p>
  <h1>Courses &amp; Materials</h1>
  <p class="lede">All syllabi, playlists and reading lists are public on this page. Registered students also get access to the private Piazza and Gradescope spaces for discussion, homework and grading.</p>
  <p><a class="btn" href="{APPLY}">Apply (Google Form)</a> <a class="btn yt" href="{YOUTUBE}" target="_blank" rel="noopener">{YT_ICON} All Lectures on YouTube</a></p>
</header>

<h2>Course Sequence</h2>
<div class="grid">
  <div class="card"><h4>Beginning</h4><h3>0 · Foundations of Mathematics</h3><p class="meta">Logic, set theory, construction of the number systems — Tao, <em>Analysis I</em>, Appendix &amp; Ch. 1–5</p></div>
  <div class="card"><h4>1st Semester</h4><h3>1 · Analysis I</h3><p class="meta">Tao, <em>Analysis I</em>, Ch. 6–11 (follow-up: <em>Analysis II</em>)</p></div>
  <div class="card"><h4>1st Semester</h4><h3>2 · Linear Algebra</h3><p class="meta"><em>Linear Algebra Done Right</em>, following Axler’s lectures</p></div>
  <div class="card"><h4>1st Semester</h4><h3>3 · Abstract Algebra</h3><p class="meta">Fraleigh, <em>A First Course in Abstract Algebra</em></p></div>
  <div class="card"><h4>1st Semester</h4><h3>4 · Statistics</h3><p class="meta">Freedman–Pisani–Purves, <em>Statistics</em> (4th ed.)</p></div>
  <div class="card"><h4>3rd Semester</h4><h3>5 · Functional Analysis</h3><p class="meta">Lax, <em>Functional Analysis</em>, with Landim’s video lectures</p></div>
</div>

<div class="read" style="padding:0">
<h2 id="foundations">0 · Foundations of Mathematics</h2>
<p>A rigorous introduction to proof, set-theoretic foundations and number systems, followed by axiomatic set theory and mathematical logic with an on-ramp to AI and knowledge representation. <strong>Prerequisites:</strong> precalculus/calculus and readiness to write proofs.</p>
<p><strong>Lectures:</strong> Dr. Ramasinghe — Manta Institute YouTube playlist.</p>
<p>{yt("https://youtube.com/playlist?list=PLyJ3cIWJvH2xMFMewVrmtZUjO14xT7O56","Watch Playlist")}</p>
<div class="grid">
  <div class="card"><h4>Part I</h4><h3>Mathematical Reasoning</h3><ul><li>Statements &amp; proofs: logic, quantifiers, induction</li><li>Sets, functions, relations, bijections</li><li>Counting: pigeonhole, binomial identities, recursion</li><li>Axioms for number systems; Peano</li><li>Sequences: monotone and Cauchy previews</li></ul></div>
  <div class="card"><h4>Part II</h4><h3>Number Systems</h3><ul><li>Natural numbers: induction &amp; recursion</li><li>Integers &amp; rationals via equivalence classes</li><li>Reals via Cauchy sequences; LUB property</li><li>Dedekind cuts</li><li>p-adic numbers &amp; Ostrowski’s theorem</li></ul></div>
  <div class="card"><h4>Part III</h4><h3>Axiomatic Set Theory</h3><ul><li>ZFC: building mathematics in ZFC</li><li>Ordinals, transfinite induction</li><li>Cardinals and their arithmetic</li><li>Axiom of Choice, Zorn’s Lemma, Well-Ordering</li></ul></div>
  <div class="card"><h4>Part IV</h4><h3>Logic &amp; Knowledge Representation</h3><ul><li>Propositional &amp; first-order logic; compactness</li><li>Modal logic primer</li><li>Logic &amp; AI</li><li>Introduction to Lean; mathematics with AI</li></ul></div>
</div>
<p>Future admission may require submitting homework and passing an exam based on these lectures.</p>

<h2>1 · Analysis I</h2>
<p>Chapters 6–11 of Terence Tao’s <em>Analysis I</em>; a follow-up course covers <em>Analysis II</em>. Piazza and Gradescope access upon acceptance.</p>

<h2>2 · Linear Algebra</h2>
<p><em>Linear Algebra Done Right</em>, following the author’s lectures. Prepares students for <a href="https://mathinmoscow.org/courses/">courses at Math in Moscow</a> and the Linear Algebra component of the <a href="https://math.indiana.edu/student-portal/graduate/phd/exams/tier-1-exams/index.html">Indiana University Tier I PhD qualifying exams</a>, and builds foundations for Abstract Algebra, Number Theory, Analysis II, Functional Analysis, Differential Geometry, AI and Machine Learning.</p>
<p>{yt("https://youtube.com/playlist?list=PLGAnmvB9m7zOBVCZBUUmSinFV0wEir2Vw","Axler Lecture Playlist")}</p>

<h2>3 · Abstract Algebra</h2>
<p>John B. Fraleigh, <em>A First Course in Abstract Algebra</em>. Prepares students for <a href="https://mathinmoscow.org/courses/advanced-algebra/">Advanced Algebra at Math in Moscow</a> and the algebra portion of the IU Tier I exams. Live online lectures on Zoom (Saturdays &amp; Sundays, 5–8 pm Sri Lanka time), recorded to YouTube; Piazza for discussion and Gradescope for homework.</p>

<h2>4 · Statistics</h2>
<p><em>Statistics</em> (4th ed.) by Freedman, Pisani and Purves. In-person lectures at Apex Campus, Nugegoda; discussion and homework on Google Classroom.</p>
<p>{yt("https://youtube.com/playlist?list=PLyJ3cIWJvH2yeUdKNUEQ7mhvLbV0vsQGu","Recorded Lectures")}</p>

<h2>5 · Functional Analysis</h2>
<p>Fully online. Primary video lectures by Claudio Landim (≈50 minutes each), three per week for twelve weeks. Weekly homework via Gradescope, a midterm and final, and a weekly Zoom discussion session.</p>
<p><strong>Texts:</strong> Peter Lax, <em>Functional Analysis</em>; Eberhard Zeidler, <em>Applied Functional Analysis</em>; Springer UTX <em>Functional Analysis</em> (reference).</p>
<p>{yt("https://youtu.be/OonaUALrKUk","Start Lecture 1")} <a class="btn ghost" href="https://w3.impa.br/~landim/Cursos/AF.pdf">Landim Notes (PDF)</a></p>

<div class="note"><strong>How to join.</strong> Apply through the Prep Program form. On acceptance you’ll receive invitations to the Piazza class (M001) and Gradescope.<br><br><a class="btn" href="{APPLY}">Apply to the Prep Program</a></div>
</div>
</div>
"""
page("courses.html", "Courses", "Courses of the Manta Institute for Mathematics: Foundations, Analysis, Linear Algebra, Abstract Algebra, Statistics and Functional Analysis — with public syllabi and lecture playlists.", courses)

# ---------------------------------------------------------------- JOURNEY
def stage(n, title, body, exits=""):
    return f'<li><b>{title}</b>{body}{exits}</li>'
def ex(label, text):
    return f'<div class="exit"><strong>{label}</strong> {text}</div>'
journey = f"""
<div class="read">
<header class="page-head">
  <p class="kicker">The Journey</p>
  <h1>The Long Journey Ahead</h1>
  <p class="lede">What I have in my mind, written down now that I’m away from Sri Lanka. My older students have heard these things many times.</p>
</header>

<p>I want one of the Manta Fellows to win the Fields Medal in my lifetime — and most of you to earn a research mathematics position at an R1 institution. No one from Sri Lanka who stayed after A/Ls has done this yet. I truly believe it is possible. Mathematics is an individual sport, like cricket.</p>
<p>India already has an Abel Prize winner who did his PhD at home: S. R. Srinivasa Varadhan received his doctorate from the <a href="https://en.wikipedia.org/wiki/Indian_Statistical_Institute">Indian Statistical Institute</a> in 1963 under <a href="https://en.wikipedia.org/wiki/C_R_Rao">C. R. Rao</a>, who arranged for <a href="https://en.wikipedia.org/wiki/Andrey_Kolmogorov">Andrey Kolmogorov</a> to be present at his thesis defence.</p>

<h2>The goal: a research position at an R1 institution</h2>
<p>These are professional mathematicians — people who get paid to prove new theorems. Here are the stages, starting from admission to a PhD program.</p>

<ol class="steps">
{stage(1,"Go to a good PhD program and pass qualifying exams.",
 "<p>Your goal is to prove a theorem. Don’t rule out applied mathematics — there are theorems in applied mathematics, statistics, theoretical physics, even biology. Mathematics is the study of structures: when new structures appear in any area, they must be written properly, and if they don’t yet exist in mathematics, new structures must be built and theorems proved about them.</p>",
 ex("Exit →","If you fail — typically after two years — you leave with an M.Sc. and can start again at another program. Some instead pursue a PhD simply to climb university ranks at home. These are <em>not</em> the mentors you want if you want to prove a theorem: people who build simple models with basic undergraduate mathematics, who “prove” big theorems with simple methods in non-peer-reviewed journals, or who write essays about mathematics for a Math Ed PhD. Many people won’t notice the difference. You should learn to spot it."))}
{stage(2,"Pick an area and an advisor, and solve a problem.",
 "<p>Work under your advisor for 3–4 years and solve an actual problem.</p>",
 ex("Exit →","It’s rare to leave without a PhD after passing qualifying exams. Some write a thesis on a problem the advisor solved long ago, or graduate on the “promise” of returning home."))}
{stage(3,"Show you can move forward — and get a postdoc.",
 "<p>If you solve a real problem and show the ability to keep going, your advisor will typically work with colleagues to find you a postdoc position.</p>",
 ex("Exit A →","Industry. Expect about six months of learning, but there are high-end industries that welcome mathematics PhDs.") +
 ex("Exit B (old) →","Return to Sri Lanka and join a university, often without even publishing the thesis.") +
 ex("Exit B (new) →","Return to Sri Lanka and join the Manta Institute: train the next generation, continue your research, publish, and be paid through research funding — without working under people who have never proved a theorem."))}
{stage(4,"Finish the postdoc — sometimes more than one.",
 "<p>You work under a professor who hired you for your PhD expertise; you learn theirs quickly, adding a new dimension to your own. My PhD was in Harmonic Analysis and my postdoc in Spectral Function Theory. My advisor, Prof. Ciprian Demeter, did his PhD in Ergodic Theory and learned Harmonic Analysis working with C. Thiele and T. Tao at UCLA.</p>",
 ex("Exit →","I took this path: I burned out at Caltech and left. Building the Manta Institute for future Sri Lankan students following the path I took feels like my call to a second adventure."))}
{stage(5,"Get a tenure-track position (Assistant Professor).",
 "<p>You have six years, evaluated annually. This is the toughest part: you lead your own research with a unique combination of expertise and form a new small sub-area. Prof. Demeter used Harmonic Analysis to solve problems in Restriction Theory with applications to Number Theory — “decoupling.” Some people don’t get tenure after six years.</p>",
 ex("Exit →","Tenure (Associate Professor) at a lower-ranked university. Prof. Michael Lacey, a giant of Harmonic Analysis, moved from IU to Georgia Tech — and spoke at the ICM the year after proving the boundedness of the bilinear Hilbert transform."))}
{stage(6,"Tenure at an R1 university — the goal.",
 "<p>No one from Sri Lanka who stayed after A/Ls has reached this level. You now have a permanent research position, likely near age 40. These positions exist to carry out very long projects — even 20–30 years — without fear of losing your job. Your salary still depends on grants, which depend on what you publish. A breakthrough at this stage, before 40, brings a Fields Medal.</p>",
 ex("Exit →","Some relax and stop researching once permanent. Don’t pick them as advisors — choose an energetic Assistant Professor or a Professor with a strong track record."))}
{stage(7,"Full Professor.",
 "<p>Keep working and you become a Professor of Mathematics, running your own research program with students and postdocs.</p>")}
{stage(8,"Emeritus Professor.",
 "<p>Some stay on after retirement, writing monographs and textbooks. There are exceptions: Prof. Ciprian Foias was doing pull-ups and proving theorems in his 80s; Prof. Jean Bourgain was at the front of the most technical parts of analysis his whole career.</p>")}
</ol>

<div class="note">The Abel Prize has no age limit — and sometimes it takes the mathematical community 40 years to realise what you did was important. Srinivasa Varadhan won it. Our own Muralitharan is the greatest bowler in cricket history. <em>[Your name]</em> will be the first Sri Lankan mathematician to win the Abel Prize — and I, Dr. Prabath Silva, absolutely believe one of you will get there.</div>
<p><a class="btn" href="{APPLY}">Start with the Prep Program</a></p>
</div>
"""
page("journey.html", "The Journey", "The stages of a research mathematician's career, from PhD to tenure — and why the Manta Institute believes a Sri Lankan will win the Abel Prize.", journey)

# ---------------------------------------------------------------- 404 + redirects
page("404.html", "Page not found", "Page not found.", """
<div class="read"><header class="page-head"><p class="kicker">404</p><h1>This page has moved</h1>
<p class="lede">The Manta Institute website has been rebuilt, and some older pages were retired.</p></header>
<p><a class="btn" href="/">Go to the home page</a> <a class="btn ghost" href="/courses">Courses</a></p></div>""")

redirects = {
    "home": "/", "about-the-founder": "/about#founder", "why-100-is-enough": "/about#why-100",
    "about-page": "/about", "about-page-for-math-people": "/about", "courses-fall-2025": "/courses",
    "foundations-of-mathematics": "/courses#foundations", "curriculum": "/courses", "detailed-curriculum": "/courses",
    "manta-protect": "/", "manta-protect-roadmap": "/", "phd-verification-project": "/", "facebook-landing-page": "/", "mentorship": "/about",
    "mentorship-1": "/about", "funding-page": "/about", "manta-blog": "/",
}
for slug, target in redirects.items():
    with open(os.path.join(OUT, slug + ".html"), "w") as f:
        f.write(f'<!doctype html><meta charset="utf-8"><title>Redirecting…</title>'
                f'<link rel="canonical" href="https://www.mantainstitute.org{target}">'
                f'<meta http-equiv="refresh" content="0; url={target}"><a href="{target}">Continue</a>')

with open(os.path.join(OUT, "CNAME"), "w") as f:
    f.write("www.mantainstitute.org\n")
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write("User-agent: *\nAllow: /\nSitemap: https://www.mantainstitute.org/sitemap.xml\n")
urls = ["", "about", "courses", "journey"]
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
            "".join(f"  <url><loc>https://www.mantainstitute.org/{u}</loc></url>\n" for u in urls) + "</urlset>\n")
print("built")

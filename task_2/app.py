from flask import Flask, request, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

DATA_SOURCE = 'candidates.json'

app = Flask(__name__)

@app.route('/')
def page_index():
    candidates = load_candidates_from_json(DATA_SOURCE)
    return render_template('index.html', candidates=candidates)

@app.route('/candidate/<int:id>')
def page_candidate(id):
  candidate = get_candidate(id, DATA_SOURCE)
  return render_template('card.html', candidate=candidate)

@app.route('/search/<candidate_name>')
def page_search(candidate_name):
  candidates = get_candidates_by_name(candidate_name, DATA_SOURCE)
  count = len(candidates)
  return render_template('search.html', candidates=candidates, count=count)

@app.route('/skill/<skill_name>')
def page_skills(skill_name):
  candidates = get_candidates_by_skill(skill_name, DATA_SOURCE)
  count = len(candidates)
  return render_template('skill.html', skill=skill_name, candidates=candidates, count=count)

app.run(debug=True)



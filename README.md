# Amutha Style Healthy Food 🍛

A Python agent that plans a healthy, tasty **Tamil home-cooking routine** every day and emails it each morning to Amutha and her family.

Amutha is a gold-medal MSc Nutrition graduate from Madurai. She wants every plate to be complete and nutritious. Her teenage children (born after 2005) love junk food. So the agent plans her healthy food, and also gives each dish a "junk-food makeover" hook: *Desi Pizza Uthappam*, *home-made Chicken 65*, a *Chicken Chapati Roll* with a curd-mint dip, *Baked Sweet Potato Wedges*, and a fortnightly **Madurai Treat Night**.

## What the morning email contains

| Time | Meal |
|------|------|
| 7:00 AM | Breakfast tiffin (millet idli, ragi dosa, pongal, adai…) |
| 10:30 AM | Fruit or fresh juice, chosen by season (mango only in mango season, guava in winter…) |
| 1:00 PM | Lunch: a protein kuzhambu or curry, a small carb base (half a cup of rice, millet rice or phulka), a vegetable poriyal, and curd or neer mor |
| 5:00 PM | **Soup for the children** plus a healthy snack |
| 8:00 PM | Dinner tiffin (or Treat Night) |
| 9:30 PM | Bedtime drink (manjal paal, ragi malt, badam milk…) |

Below the menu, **Today's Recipes** gives a full recipe for every dish of the day: ingredients with quantities for 4 people (2 adults + 2 teenagers), step-by-step method, cooking/soaking time and a tip. Each recipe is complete on its own, including its chutney, sambar or rasam.

It also includes the Tamil name and a nutrition note for every dish, a tip for getting the children to eat, prep for the next day (soaking, batter, marinating), today's ingredient list, and a countdown to the next Treat Night.

## Amutha's rules and how the code enforces them

| # | Rule | How it is enforced |
|---|------|--------------------|
| 1 | Maida once in two weeks only | Only the 3 `MAIDA_TREAT` dishes contain maida, and they are served on exactly one night every 14 days. Any other dish that lists maida fails the check. |
| 2 | Less rice | Half a cup of rice on 3 or 4 lunches a week. Other days use millet rice or phulka. On rice days the breakfast and dinner have no rice, and the daily rice score is capped. |
| 3 | More fish and chicken than mutton; no beef or pork | Fixed fortnight rhythm: fish 5×, chicken 4× (one is biryani), egg 2×, dal 2×, mutton 1× per 14 days. Beef, pork, ham and bacon are banned words. |
| 4 | One soup every day for the children | There is a soup slot every day, and the check fails without one. |
| 5 | One fruit or fruit juice every day | There is a seasonal fruit slot every day, with no added sugar. |
| 6 | No processed food | Banned: packaged items, instant noodles, bread, ketchup, soup powder, MSG, food colour… Everything is home-made. |
| 7 | No cheese | `cheese` and `paneer` (paneer is a fresh cheese) are banned. |
| 8 | No shop mayonnaise | Banned. Wraps and rolls use a home-made hung-curd and mint dip. |
| 9 | Good vegetables | Every lunch has a vegetable poriyal or kootu, and the soups, sambars and kurmas are vegetable-based. |
| 10–11 | Indian food only, Tamil preferred | Every dish is tagged `tamil` or `indian`. Most are Tamil and Madurai classics. |
| 12 | Spice is fine but must not burn the children's tongues | Spice level is capped at 2 (medium). Tips suggest a separate chilli tadka for adults. |

On every run, `plan_with_checks()` checks the 27 days around the date against all the rules (`amutha_agent/rules.py`). **If any rule would be broken, no email is sent.** The tests check two full years of menus.

## Quick start

```bash
pip install -r requirements.txt     # anthropic is optional; the rest is standard library
cp .env.example .env                # fill in emails + Resend API key

python -m amutha_agent              # print today's menu
python -m amutha_agent --week       # 7-day preview
python -m amutha_agent --date 2026-10-31 --html menu.html   # preview a day as HTML
python -m amutha_agent --send       # print and email it
python -m pytest -q                 # run the rule tests
```

### Email setup with Resend (default)
1. Sign up at [resend.com](https://resend.com) and create an API key → `RESEND_API_KEY`.
2. Verify a domain you own under *Domains* (add the DNS records Resend shows). Then use an address on it as
   `EMAIL_FROM`, for example `Amutha's Kitchen <kitchen@yourdomain.com>`.
   *Without a domain you can test with `onboarding@resend.dev`, but Resend then only delivers to the email
   address of your own Resend account. To reach the whole family you need a verified domain.*
3. Put Amutha in `AMUTHA_EMAIL` and everyone else, comma-separated, in `FAMILY_EMAILS`.

The agent calls Resend's REST API with the Python standard library, so it needs no extra package.

**Free setup without a domain:** set `EMAIL_FROM=onboarding@resend.dev` and put your own Resend sign-up
address in `AMUTHA_EMAIL` and `FAMILY_EMAILS`. The menu then reaches only you, at no cost. To reach other
people for free, use Gmail SMTP below.

### Email setup with SMTP (alternative)
Set `EMAIL_PROVIDER=smtp` and fill in `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER` and `SMTP_PASSWORD`. For Gmail,
turn on 2-step verification and create an **App password**.

## Sending it every morning automatically

**Option A: GitHub Actions (no computer needs to stay on).**
`.github/workflows/daily-menu.yml` runs every day at about **05:07 IST** (GitHub can start scheduled jobs a little late). In the repository go to *Settings → Secrets and variables → Actions* and add `AMUTHA_EMAIL`, `FAMILY_EMAILS`, `RESEND_API_KEY`, `EMAIL_FROM`, and optionally `ANTHROPIC_API_KEY`. (For SMTP instead, add `EMAIL_PROVIDER=smtp` plus the `SMTP_*` secrets.) You can also start it by hand from the *Actions* tab ("Run workflow").

**Option B: a home computer or server.**
```bash
python -m amutha_agent --daemon      # sends daily at SEND_TIME in TIMEZONE
# or with cron (05:30 IST):
30 5 * * * cd /path/to/HealthyFoodRoutine_Claude && python3 -m amutha_agent --send
```

## Optional AI chef note (Claude)

If `ANTHROPIC_API_KEY` is set, the agent asks Claude for a short, fun note for the teenagers: serving ideas and a line to say at the table. It only covers dishes already on the menu. The menu itself always comes from the rule-checked planner. The note is screened for banned words before it goes into the email, and it is skipped silently if there is no key or the call fails. Turn it off with `AI_CHEF=off` or `--no-ai`.

## Project layout

```
amutha_agent/
  dishes.py    # ~115 home-made Tamil/Indian dishes with nutrition notes and kid hooks
  recipes/     # a full recipe (ingredients + method) for every dish, by meal
  rules.py     # Amutha's 12 rules as code (dish checks + multi-day checks)
  planner.py   # fortnight rhythm + rotating dish lists; same menu for the same date
  render.py    # plain-text and HTML email
  emailer.py   # sending via Resend (default) or SMTP
  ai_chef.py   # optional Claude note for the children
  config.py    # settings from environment / .env
  cli.py       # command line + daemon
tests/         # two years of menus checked against every rule
```

### Changing the menu
Add or edit dishes in `amutha_agent/dishes.py`, and give each new dish a recipe in `amutha_agent/recipes/`. Run `python -m pytest -q` afterwards. The tests will tell you if the new dish breaks a rule, for example by listing cheese or being too spicy.

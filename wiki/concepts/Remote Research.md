---
type: concept
name: Remote Research
created: 2026-07-31
updated: 2026-09-10
status: developed
aliases:
  - "Remote Testing"
---

# Remote Research

## Definition

Remote research covers user-research methods in which the researcher and the
participant are not in the same place. The sources treat it as two distinct
families rather than one method. In **remote moderated** studies a facilitator is
present over video: they can change, skip and reorder tasks, ask follow-ups,
encourage thinking aloud, and run roughly hour-long sessions
[[2020-04-12_moderated-remote-usability-test-why]]. In **remote unmoderated**
studies there is no facilitator at all: tasks are set up in a testing tool and
participants complete them asynchronously while the tool records screen, voice
and transcript [[2019-10-27_unmoderated-usability-testing]]
[[2024-12-06_unmoderated-user-testing-tools]].

Its appeal is the removal of geographic and cost barriers: participants can be
anywhere [[2024-12-06_unmoderated-user-testing-tools]], and remote moderated
testing is presented as a middle ground delivering findings comparable to
in-person while staying as convenient and inexpensive as unmoderated
[[2020-04-12_moderated-remote-usability-test-why]]. The recurring costs are
equally consistent across the sources: less control over the participant and
their environment [[2020-08-23_problem-participants-remote-unmoderated]], more
technical setup to arrange in advance [[2022-11-13_remote-contextual-inquiry]]
[[2022-08-28_testing-ar-apps]], and more exposure of participant data through
third-party tools [[2022-09-04_privacy-and-security]].

## Practice

### Choosing between moderated and unmoderated

[[2020-04-12_moderated-remote-usability-test-why]] compares in-person moderated,
remote moderated and remote unmoderated across eight dimensions and argues for
the middle option when the goal is deep, rich insight, when participants are
geographically distributed or unable to travel, and when researchers have the
time for individual sessions. Its stated advantages: facilitators can adapt the
protocol live, ask for elaboration, coach think-aloud, and run about an hour;
having a facilitator present makes the session feel more natural and reduces
multitasking and environmental distraction; and teams can observe simultaneously
and debrief immediately, cutting analysis time. It lists the unmoderated
drawbacks symmetrically — sessions typically capped around 20 minutes, no way to
clarify an ambiguous instruction or ask a follow-up, unrepresentative testers,
and variable motivation and focus.

[[2019-10-27_unmoderated-usability-testing]] argues the other side on its own
terms: with no meetings to schedule, a study can launch and return results within
hours, from dozens or hundreds of simultaneous participants. Its limits are
scoped rather than general — early-stage prototypes are hard to test without a
moderator to explain and to recover from errors, and participants are less
engaged, therefore less realistic, on tasks requiring imagination,
decision-making or emotional response. It is best suited to live sites, apps and
highly functional prototypes.

### Compensating for the missing moderator

Because no human can adapt the procedure on the fly, unmoderated research
requires even more meticulous planning than a moderated study
[[2019-10-27_unmoderated-usability-testing]]. Concretely: task instructions must
be exceptionally clear, specific and actionable, must avoid hints, and must state
explicitly when to stop — the article names task writing as where most
researchers fail to get the results they need. Pilot testing is not optional: run
it with real participants on their own equipment to surface problems with
wording, task sequence, prototype functionality and technical limits before
launch.

### Guarding data quality

[[2020-08-23_problem-participants-remote-unmoderated]] establishes that problem
participants are more common in remote unmoderated studies than in remote
moderated or in-person ones, precisely because no facilitator is watching, and
splits them into three types: outliers (behaving differently because they are
different users, not because they cheat), cheaters (interested only in payment,
clicking randomly without attempting tasks), and professional participants (too
frequent, too attuned to researcher goals).

Detection differs by study type. Qualitatively, watch recordings for signals:
mismatched experience or motivation for outliers; ignored instructions and
unattempted tasks for cheaters; insider vocabulary such as "kerning", "mental
model" or "hamburger" for professionals. Quantitatively, use frequency
distributions of task time and task success — low success combined with very fast
times is a strong cheater indicator — and read open-ended text for nonsense
keyboard mashing.

Removal decisions are graded: remove genuinely unrepresentative outliers
completely, but an unfavourable reaction to the design is not by itself grounds
for exclusion; for cheaters, drop the affected tasks or the whole session, and
note that most remote testing tools offer free cheater replacement; professional
participants who actually showed up and participated should generally be kept,
flagged in the analysis, and screened out of future studies via a 0-3 or 0-6
month participation exclusion.

### Remote contextual inquiry

[[2022-11-13_remote-contextual-inquiry]] shows that in-situ observation survives
the move to video: the participant stays in their natural context while the
researcher observes through video call and screen share, which removes access,
travel and safety barriers while still revealing natural distractions,
workarounds and interruptions. The fit is narrow — computer-based, desk-bound
knowledge work visible on a single shareable display, with minimal physical
movement.

Its operational lessons for remote work generally: communicate technical
requirements (screensharing, firewall restrictions, recording permissions)
upfront and rehearse the setup in a 10-minute call beforehand; explicitly stress
your interest in the participant's typical environment, or well-meaning
participants will relocate to somewhere quieter and tidier; cap sessions at 2-3
hours because remote attention is more taxed, splitting observation from
discussion; turn the researcher's camera off during observation so the
participant stops reading your face and slips into flow; record for later
analysis; watch for environmental cues and off-screen attention; use active
inquiry to probe in real time since details are harder to recall remotely;
improvise with guided tasks when flow is hard to reach; and schedule follow-up
sessions for long workflows.

### Remote testing of spatial and physical experiences

[[2022-08-28_testing-ar-apps]] extends remote practice to augmented reality,
where the participant moves through their own physical space. That requires
communicating space requirements in advance, obtaining consent for recording the
surroundings and not just the screen, and being able to help participants
troubleshoot AR features from a distance. Related preparation the article
recommends: unambiguous task wording (participants new to AR misread tasks — "take
a photo of animals" may be read as real pets), ample hazard-free space since
participants focused on virtual objects ignore their surroundings, longer
sessions to absorb app downloads and AR learning (have participants download
15-20 minutes ahead or start the download at the session opening), recording both
the phone screen and the participant's movement via a tripod-mounted camera with
a wearable microphone for audio, screening for age, health, physical ability and
glasses, and telling participants in advance about the physical activity and
their right to withdraw. It also asks for extra patience with participants
unfamiliar with AR patterns.

### Privacy and security obligations

[[2022-09-04_privacy-and-security]] flags remote studies specifically: relying on
third-party tools and online platforms raises data-breach risk, so researchers
must assess tool security and keep control over how data is stored and shared.
Its practices apply across the study lifecycle — establish data-management
guidelines (consent, storage, sharing, breach response, deletion) before the
study and update them as laws change; justify every piece of identifiable data
before collecting it; choose secure tools up front to avoid fragmentation and
avoid public cloud storage such as Google Drive or Dropbox for sensitive data,
using secure file transfer instead; keep names out of notes and file names, pause
recording during sensitive input such as passwords and addresses, and blur or
delete identifying material; and use consistent naming and storage so data can
actually be found and deleted when the study is over. The article distinguishes
confidentiality (private but linked to identity) from anonymity (unlinked), and
argues these practices belong in ResearchOps workflows so privacy scales without
burdening individual researchers.

### Tooling for unmoderated studies

[[2024-12-06_unmoderated-user-testing-tools]] compares 11 platforms as of
September 2024. All of them record participant screen and voice, allow timestamped
notes, auto-generate transcripts, and support downloading recordings or clips.
All but Maze support live websites, prototypes and mobile apps on iOS or Android.
Most include their own participant panel or integrate with third-party recruiters
such as User Interviews. Pricing follows pay-as-you-go, subscription or
enterprise models, with older feature-rich platforms generally costing more than
newer basic ones. Differentiators to select on include webcam recording, AI
transcription, highlight reels, randomization, skip logic and statistical
analysis; most of these tools now sit inside broader research platforms covering
methods beyond unmoderated testing.

## Sources (8)

- [[2019-10-27_unmoderated-usability-testing]] — details the unmoderated remote testing approach, contrasting it with moderated remote testing and in-person methods.
- [[2020-04-12_moderated-remote-usability-test-why]] — advocates remote moderated testing as a viable alternative to in-person testing that maintains research quality while reducing geographic and cost barriers.
- [[2020-08-23_problem-participants-remote-unmoderated]] — Remote unmoderated studies are particularly susceptible to problem participants due to lack of direct facilitator oversight, requiring systematic screening methods to maintain data quality.
- [[2022-08-28_testing-ar-apps]] — Remote AR testing requires communication about space requirements, recording of surroundings with participant consent, and ability to help participants troubleshoot AR features remotely.
- [[2022-09-04_privacy-and-security]] — Remote studies using third-party tools and online platforms increase data-breach risks; researchers must assess tool security and maintain control over data storage and sharing.
- [[2022-11-13_remote-contextual-inquiry]] — remote research requires clear upfront communication about technical requirements, intentional setup practices, and adaptation of session structure for virtual attention spans and dynamics.
- [[2024-12-06_unmoderated-user-testing-tools]] — Discusses how unmoderated tools enable participants located anywhere to complete studies online, providing flexibility and access to distributed user populations.
- [[2016-11-04_ux-research_07-chapter-6-logistics]] — handling technical constraints of online sessions, training participants on conferencing tools, and planning contingencies.

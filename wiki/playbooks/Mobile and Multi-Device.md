---
type: playbook
name: Mobile and Multi-Device
theme: Mobile and Multi-Device
created: 2026-08-21
updated: 2026-08-21
status: active
sources_as_of: 2026-07-31
concepts:
  - Mobile Design
  - Discoverability
  - Responsive Design
  - Augmented Reality
  - Voice Interfaces
  - Smart Devices
---

# Playbook — Mobile and Multi-Device

Checkable rules distilled from this theme's concept pages, for
`product-wiki-review`. Give each one a verdict: `holds`, `breached`, or `n/a`
with a reason.

A **cache** of [[Mobile and Multi-Device]] (`docs/adr/0004`), not a
replacement. Open the concept page when a rule needs its nuance.

Mobile is treated throughout as **its own medium**, not a smaller desktop: its
own input (fingers, not a cursor), its own constraints (screen space, network,
interrupted attention) and its own capabilities (camera, GPS, biometrics) that
desktop lacks. [[Mobile Design]]

## Porting is the named failure mode

**M1. A pattern is not carried unchanged between platforms.**
Desktop layouts converted to mobile produce unreadable images and untappable
targets; mobile patterns pushed onto desktop produce hidden navigation and
wasted space. Mobile-first is a prioritisation discipline, not a licence to
design once and ship everywhere. [[Mobile Design]]

**M2. Hidden navigation is measured, not assumed neutral.**
Hidden navigation dropped content discoverability 20%, made tasks rated 21%
more difficult, and cost 39% more time on desktop, 15% on mobile, in direct
comparison against visible and combo navigation. Accessing it cost 5-7 extra
seconds on desktop, 2 on mobile. [[Discoverability]] [[Mobile Design]]
*Caveat, dated:* by 2023 hamburger menus were reported as a converged,
expected pattern on mobile specifically — the finding above concerns
carrying hidden nav to desktop, not mobile use itself. [[Mobile Design]]

**M3. Responsive design is a delivery technique, not a design decision.**
Content reflowing across sizes does not mean the same interactions work
everywhere; simply rewrapping desktop content for a small screen does not
produce a usable mobile interface. [[Responsive Design]]

**M4. Breakpoints come from the audience's real device distribution, not a
standard preset.** A common convention: extra-small mobile to ~500px, small
tablet 500-1200px, medium laptop 1200-1400px, large 1400px+. Foldables break
the model further: test on real devices and keep the folded and unfolded
states consistent, or users must relearn the interface each time they fold.
[[Responsive Design]]

## Touch and gesture

**M5. Touch targets are at least 1cm × 1cm as physically rendered.**
Pixel dimensions are meaningless across densities. Size and spacing both
matter: packed large targets and well-spaced tiny ones both fail. Primary
actions, apps used while moving, and interfaces for children or seniors need
more than the minimum. [[Mobile Design]]

**M6. A gesture is invisible unless something signals it.**
Gestures have no visual representation by default, so they are hard to
discover and remember. Apps built almost entirely on undiscoverable gestures
failed with general users despite design-community praise. A residual visual
signifier (the iPhone X home line) and frequent repetition are what make a
gesture viable. [[Mobile Design]]

**M7. Contextual swipe reveals content the user can still see, and its
meaning stays stable.** Users forget to try it, revealed actions can obscure
the item being acted on, and a nonstandard meaning (saving rather than
deleting) goes undiscovered. Reserve swipe for deletion and removal, confirm
destructive actions or offer easy undo. [[Mobile Design]]

**M8. Drag-and-drop is treated as weak on touch.**
No hover states to carry a signifier, imprecise fingers, and taps versus
swipes to disambiguate. A menu-based alternative costs more steps but produces
fewer errors. [[Mobile Design]]

**M9. Overlay dismissal offers one clear, visible way out.**
Close button, tap-outside, swipe-down and the device back button coexisting
without signalling which applies is a documented cause of lost work: users
guess wrong. Avoid stacking overlays; keep a visible close button; support the
device back button. [[Mobile Design]] [[Discoverability]]

## Layout and content

**M10. Images are re-cropped for mobile, not merely resized.**
Simple resizing produces disproportionate scaling, loses subjects to
cropping, or shifts an image's relationship to nearby text. Remove low-value
images; keep only those that carry real meaning, deliberately reframed.
[[Mobile Design]]

**M11. A sticky header stays as small as the readable minimum, with real
contrast against the content.** Consider whether it needs to be sticky at
all, and if it hides on scroll-down, animate the return over 300-400ms.
[[Mobile Design]]

**M12. A mobile table is re-designed, not shrunk.**
Stick column headers and row labels, signal horizontal scroll with a visible
cut or arrow rather than dots, and give users filters or column toggles to
control what they see. Make the desktop table right first — the mobile
constraint often reveals improvements that help everyone. [[Mobile Design]]
[[Responsive Design]]

**M13. A carousel reaches its last item in three or four steps, or it should
be a list instead.** Use edge-peeking content or arrows as the continuation
signal, not dots; support horizontal swipe with gutters to reduce ambiguity.
[[Mobile Design]]

**M14. Visual indicators are not "decluttered" away.**
Colour-plus-icon indicators outperform every alternative on mobile; text-only
runs 57% slower to completion. Removing them to declutter removes real
signal. [[Mobile Design]]

## Interruption and attention

**M15. The design accounts for sessions under 15 seconds.**
Over 40% of mobile usage is microsessions. Four entry points let users
bypass launching the app at all: notifications, widgets, quick actions
(long-press), voice. Notifications and widgets must be self-sufficient and
untruncated. [[Mobile Design]]

**M16. A constrained or embedded app variant still keeps the core task
reachable**, or hands off cleanly to the full app, and leans on the host
platform's own strengths rather than reproducing them. [[Mobile Design]]

## Onboarding on mobile

**M17. A deck-of-cards tutorial is not assumed to help.**
Measured directly: 91% task success for users who read a first-launch
tutorial versus 94% for those who skipped it, comparable completion time, and
the tutorial group rated the task as *more* difficult. [[Mobile Design]]

**M18. Onboarding is reserved for genuinely unfamiliar interaction, not
conventional ones.** Instruction is wasted on a conventional interface and
needed for a new interaction pattern (AR is the clear case where walkthroughs
help). Where used, favour minimal, optional, contextual instruction over an
upfront sequence. [[Mobile Design]]

**M19. A permission request explains its benefit, in context, at first
relevant use.** Giving a reason raised grant rate 12%; framing that reason
around user benefit rather than system need raised it 81% further. Asking at
launch, before context, underperforms asking when the user reaches the
feature that needs it. [[Mobile Design]]

## Augmented reality and voice

**M20. AR is promoted where it can be seen, with a text label, not an
icon alone.** Most users do not look for AR by default and confuse it with
VR; the AR cube icon is not reliably recognised. [[Augmented Reality]]

**M21. AR instructions specify device handling explicitly**: angle, height,
distance, lighting, surface — many users do not realise the camera drives the
experience at all. Keep critical controls at the bottom of the screen, where
attention concentrates during AR use. [[Augmented Reality]] [[Mobile Design]]

**M22. Voice interaction states what it can do, since there is no visible
menu to scan.** Discoverability without a screen depends entirely on audio
signifiers: earcons, explicit verbal options, or implicit cues. Ration them —
long enumerated option lists are forgotten before the user reaches the end.
[[Voice Interfaces]]

**M23. A short, simple task is a good fit for voice; a repetitive
multi-step one is not.** A single misheard command can make a short voice task
slower than the physical alternative. [[Voice Interfaces]]

## Smart devices and companion apps

**M24. Setup and reconnection get the same guided treatment.**
Users rarely remember infrequent setup steps, so a reconnection after a power
or network outage deserves the same visual, step-by-step guidance as first
use. Progress indicators must reflect real progress: a bar that fills without
meaning destroys trust. [[Smart Devices]]

**M25. Every connected device's status is visible on one overview screen**,
without navigating into each device individually. [[Smart Devices]]

## Where this theme stops

Component-level control choices apply the same way on mobile as elsewhere;
see [[Interaction and Interface Patterns]]. Contrast and touch-target
accessibility rules live in [[Accessibility and Inclusion]]. Navigation
structure and menu shape live in [[Structure, Navigation and Findability]].

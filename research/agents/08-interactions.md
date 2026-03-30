# Agent 8 / 10 — Interactive Mechanisms for AI-101 HTML Slides

## Mechanism Inventory

### 1. Tabs (concept grouping)
| Attribute | Detail |
|---|---|
| **User value** | Reduces cognitive load; lets learners self-pace across related sub-topics without leaving the slide |
| **Implementation** | `<input type="radio">` + CSS sibling selector — zero JS. Or minimal JS `aria-selected` toggle |
| **Complexity** | Low (30–50 lines CSS) |
| **Pitfalls** | Deep-linking breaks (URL doesn't reflect active tab); screen-reader trap if `role="tabpanel"` omitted; avoid >5 tabs on mobile |

**Recommendation:** Use CSS-only radio pattern. Add `data-tab` attributes for optional JS deep-link support. Always wire `aria-controls` + `aria-selected`.

---

### 2. Prompt Carousel (input/output examples)
| Attribute | Detail |
|---|---|
| **User value** | Shows AI prompt diversity in one slide; learners see pattern variation without page-flip overhead |
| **Implementation** | Array of `{prompt, response}` objects; prev/next buttons swap `textContent`; optional auto-advance |
| **Complexity** | Medium (80–120 lines JS) |
| **Pitfalls** | Auto-advance fights readers; keyboard trap if focus not moved with slide change; long outputs cause reflow jank |

**Recommendation:** Disable auto-advance by default. Fix container `min-height` to largest example to prevent reflow. Add `aria-live="polite"` on output region.

---

### 3. Before / After Toggle (prompt quality comparison)
| Attribute | Detail |
|---|---|
| **User value** | Visceral "bad vs. good prompt" contrast drives retention better than static side-by-side |
| **Implementation** | Single checkbox + CSS `:checked ~ .after` show/hide; or JS class toggle |
| **Complexity** | Low (20–40 lines) |
| **Pitfalls** | Label must clearly state which state is active; color alone insufficient for diff (add icon/label); mobile — ensure tap target =44px |

**Recommendation:** Pair with a pill label ("Weak prompt / Strong prompt") that updates on toggle. Use `<button aria-pressed>` over checkbox for semantics.

---

### 4. Reveal Steps (progressive disclosure / build-up)
| Attribute | Detail |
|---|---|
| **User value** | Instructor-paced reveals prevent ahead-reading; keeps audience focus during live demos |
| **Implementation** | `data-step` attributes on child elements; keyboard (? arrow / Space) advances reveal counter; CSS `opacity/transform` transition |
| **Complexity** | Medium (60–100 lines JS) |
| **Pitfalls** | Print mode must show all steps simultaneously; step counter must reset on slide re-entry; no reveal state in URL = presenter loses place on refresh |

**Recommendation:** Add `@media print { [data-step] { opacity: 1 !important } }`. Persist step index in `sessionStorage` keyed by slide ID. Expose keyboard shortcut legend.

---

### 5. Demo Launcher (live iframe / sandbox embed)
| Attribute | Detail |
|---|---|
| **User value** | Zero context-switch — learner runs real AI interaction inside the deck; highest engagement |
| **Implementation** | `<iframe>` pointing to a sandboxed CodePen / StackBlitz / local `/demo` route; lazy-load on button click to avoid blocking slide render |
| **Complexity** | High (iframe sizing, CSP, CORS, API key handling) |
| **Pitfalls** | API keys must never appear client-side (proxy all calls through Netlify function); iframe resize on mobile breaks layout; CSP `frame-src` must whitelist domain; loading spinner needed (cold start ~2s) |

**Recommendation:** Gate the iframe behind a "Launch Demo" button (`loading="lazy"` pattern). Route API calls through `/.netlify/functions/ai-proxy`. Show skeleton loader. Provide "Open in new tab" fallback.

---

## Priority Matrix

| Mechanism | Impact | Effort | Ship Order |
|---|---|---|---|
| Before/After Toggle | High | Low | 1 |
| Reveal Steps | High | Medium | 2 |
| Prompt Carousel | High | Medium | 3 |
| Tabs | Medium | Low | 4 |
| Demo Launcher | Highest | High | 5 (post-MVP) |

## Cross-Cutting Rules
- All mechanisms must be keyboard-navigable and pass WCAG 2.1 AA.
- No mechanism should block slide navigation (trap focus carefully).
- State resets on slide exit unless explicitly persisted.
- Bundle overhead target: **< 8 KB JS total** for all five mechanisms combined — vanilla DOM is sufficient, no framework needed.

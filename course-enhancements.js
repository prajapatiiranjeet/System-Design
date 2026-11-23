(() => {
  const PLAY_ID = 'course-play';
  const REPLAY_ID = 'course-replay';
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let timer = null;
  let advancing = false;
  let activeLessonId = currentLessonId();

  function currentLessonId() {
    return window.location.hash.match(/^#\/([^/]+)/)?.[1] || null;
  }

  function stopLessonPlayback() {
    if (timer !== null) window.clearInterval(timer);
    timer = null;
    const play = document.getElementById(PLAY_ID);
    if (play) {
      play.textContent = 'Play lesson';
      play.setAttribute('aria-label', 'Play through lesson stages');
      play.removeAttribute('data-playing');
    }
  }

  function advanceStage() {
    const buttons = [...document.querySelectorAll('#timeline .timeline__steps button[data-step]')];
    if (!buttons.length) return;
    const current = buttons.findIndex(button => button.closest('li')?.classList.contains('is-current'));
    if (current < 0 || current >= buttons.length - 1) {
      stopLessonPlayback();
      return;
    }
    advancing = true;
    buttons[current + 1].click();
    advancing = false;
    if (current + 1 === buttons.length - 1) stopLessonPlayback();
  }

  function startLessonPlayback() {
    const buttons = document.querySelectorAll('#timeline .timeline__steps button[data-step]');
    if (buttons.length < 2) return;
    const play = document.getElementById(PLAY_ID);
    if (!play) return;
    play.textContent = 'Pause lesson';
    play.setAttribute('aria-label', 'Pause lesson stage playback');
    play.setAttribute('data-playing', 'true');
    const interval = reducedMotion.matches ? 1400 : 2600;
    timer = window.setInterval(advanceStage, interval);
  }

  function mountLessonControls() {
    const tools = document.querySelector('.stage__tools');
    if (!tools) return;
    if (!document.getElementById(PLAY_ID)) {
      const play = document.createElement('button');
      play.id = PLAY_ID;
      play.type = 'button';
      play.className = 'tool course-stage-action';
      play.textContent = 'Play lesson';
      play.setAttribute('aria-label', 'Play through lesson stages');
      play.addEventListener('click', () => {
        if (timer !== null) stopLessonPlayback();
        else startLessonPlayback();
      });
      tools.append(play);
    }
    if (!document.getElementById(REPLAY_ID)) {
      const replay = document.createElement('button');
      replay.id = REPLAY_ID;
      replay.type = 'button';
      replay.className = 'tool course-stage-action';
      replay.textContent = 'Replay lesson';
      replay.setAttribute('aria-label', 'Restart lesson from the first stage');
      replay.addEventListener('click', () => {
        stopLessonPlayback();
        document.querySelector('#timeline .timeline__steps button[data-step="0"]')?.click();
      });
      tools.append(replay);
    }
  }

  document.addEventListener('click', event => {
    if (timer === null || advancing || event.target.closest(`#${PLAY_ID}, #${REPLAY_ID}`)) return;
    if (event.target.closest('#timeline .timeline__steps button[data-step], #next, #back')) {
      stopLessonPlayback();
    }
  }, true);
  window.addEventListener('hashchange', () => {
    const nextLessonId = currentLessonId();
    if (activeLessonId && nextLessonId && nextLessonId !== activeLessonId) stopLessonPlayback();
    activeLessonId = nextLessonId;
  });


  function mountProgressReset() {
    const body = document.querySelector('#progress-body');
    if (!body || document.getElementById('course-progress-reset')) return;
    const reset = document.createElement('button');
    reset.id = 'course-progress-reset';
    reset.type = 'button';
    reset.className = 'course-progress-reset';
    reset.textContent = 'Reset progress';
    reset.setAttribute('aria-label', 'Reset completed lessons and saved course position');
    reset.addEventListener('click', () => {
      for (const key of ['done', 'last', 'recent']) window.localStorage.removeItem(`sdt:${key}`);
      window.location.reload();
    });
    body.append(reset);
  }

  function init() {
    mountLessonControls();
    mountProgressReset();
    const app = document.getElementById('app');
    if (!app) return;
    new MutationObserver(() => { mountLessonControls(); mountProgressReset(); }).observe(app, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init, { once: true });
  else init();
})();

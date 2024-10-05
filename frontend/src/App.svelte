<script>
  import LoadingSpinner from "./components/LoadingSpinner.svelte";
  import { onMount } from "svelte";
  import Main from "./Main.svelte";

  import {loadPyodide} from 'pyodide'

  let loaded = false;
  let time = 0;
  let error = '';

  onMount(async() => {
    let interval = setInterval(() => time += 0.1, 100)
    await loadPyodide()
    clearInterval(interval)
    


    if('serviceWorker' in navigator) {
      addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js')
      });

      loaded = true
    } else {
      error = "No service worker support in your browser."
    }
  });
</script>

{#if loaded}
  <Main />
{:else if error.length}
  <main>
    <div>
      <h1>Error</h1>
      <span class="error">{error}</span>
      <span>Try again in a more modern browser.</span>
    </div>
  </main>
{:else}
  <main>
    <div>
      <LoadingSpinner color=white />
      <h1>Cargando Python...</h1>
      <span>Necesitamos descargar unos archivos para correr Python en tu navegador</span>
      <span>Solo tomará unos segundos...</span>
      <span style="color: lightgreen; opacity: 1">Redireccionando...</span>
      <span>{time.toFixed(1)}s</span>
    </div>
  </main>
{/if}

<style>
  main {
    position: fixed;
    inset: 0;

    background: black;

    color: white;

    display: grid;
    place-items: center;

    user-select: none;
  }

  .error {
    color: #f22;
    opacity: 1;
  }

  main > div {
    display: flex;
    flex-direction: column;

    align-items: center;
  }

  main > div > span {
    opacity: .5;
  }

  main > div > span:last-of-type {
    font-style: italic;
  }
</style>
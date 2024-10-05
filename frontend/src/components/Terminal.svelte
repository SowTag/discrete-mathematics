<script lang='ts'>
  import { onMount } from "svelte";

  import { loadPyodide, type PyodideInterface } from 'pyodide'
  import LoadingSpinner from "./LoadingSpinner.svelte";
    import type { KeyboardEventHandler } from "svelte/elements";

  const BASE_URL = "https://raw.githubusercontent.com/SowTag/discrete-mathematics/refs/heads/master/modules/"

  let lines: string[] = [];

  let currentEvent = 0;
  let chooserOpen = true;
  let loading = "Esperando al intérprete";

  let modules = [
    { 
      name: "Coinflip", 
      description: "Calcula probabilidades y estadisticas en tiros de moneda",
      file: "Ejercicio.py"
    },
    {
      name: "Conteo", 
      description: "Herramienta para calcular variaciones, permutaciones, y mas. Ejemplo de overflow del texto",
      file: "combinatorics.py"
    }
  ]

  let currentModule = 1;

  let code = ""
  let py: PyodideInterface


  function handleKeydown(event: KeyboardEvent) {
    
    if(event.key === 'Enter') {
      // @ts-ignore
      lines[currentEvent++] = event.target.value
      lines = lines
      // @ts-ignore
      event.target.value = ''
      console.log(lines)
    }
  }

  onMount(async() => {
    // Have pyodide cached
    py = await loadPyodide();
    loading = "";
  })

  async function executePython() {
    // Load scope
    await py.runPython(code)

    // Run entrypoint
    let out = await py.runPython("combinatorics()")
    console.log(out)
    console.log(code)
  }

  async function useModule(id: number) {
    loading = `Cargando módulo ${modules[id].name} (${modules[id].file})`
    
    try {
      let req = await fetch(BASE_URL + '/' + modules[id].file)
      let text = await req.text()
      
      if(text) code = text
      loading = ""
      lines = []
      executePython()
    } catch(e) {
      console.error(e)
      loading = "Ocurrió un error. Volviendo al menú principal..."
      setTimeout(() => loading = "", 3000)
    }
  
  }
</script>


<main>
  {#if loading}
    <div class="loading">
      <LoadingSpinner color='greenyellow'/>
      <span>{loading}</span>
    </div>
  {/if}
  
  {#if (currentModule === -1 || chooserOpen) && !loading}
    <div class="chooser">
      <div class="header">
        <span>Selecciona uno de los módulos de abajo, y se cargarán dinámicamente de nuestro repositorio en <a href="https://github.com/SowTag/discrete-mathematics">GitHub</a>.</span>
      </div>
      {#each modules as mod, index}
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <div 
        on:click={() => useModule(index)}
        class={`module ${currentModule == index ? "selected" : ""}`}>
          <span class="name">{ (currentModule == index ? "*" : "") + mod.name}</span>
          
          <div>
            <span class="description">{mod.description}</span>
            <span class="file">{mod.file}</span>
          </div>
        </div>
      {/each}
    </div>

  {:else}
    {#each lines as line}
      <span class="line">{line}</span>
    {/each}
  {/if}


  {#if !chooserOpen}
  <div class="input">
    <input on:keydown={handleKeydown} type="text" placeholder={loading ? "" : "Esperando al intérprete de Python..."}>
  </div>
  {/if}
</main>

<style>

  .chooser {
    width: 100%;
    height: 100%;

    display: flex;

    flex-direction: column;

    color: greenyellow;

    user-select: none;
  }

  .chooser .header {
    border-bottom: 1px solid #222;
    padding: 1em;
    font-size: 1.2em;
  }

  .chooser .header a {
    text-decoration: none;
    color: cyan;
  }

  .module {
    display: flex;
    align-items: center;
    padding: 1.5em 1em;

    cursor: pointer;

    font-size: 1.1em;
  }

  .module > div {
    display: flex;
    flex-direction: column;
    width: 100%;
  }

  .module .file {
    opacity: .5;
    margin-left: auto;
  }

  .module.selected {
    border-left: 3px solid greenyellow;
  }

  .module:hover {
    background: rgba(0, 255, 0, 0.1);
  }

  .module span.name {
    font-size: 1.25em;
    font-weight: bold;

    margin-right: 1em;
  }

  .input {
    margin-top: auto;
  }

  .loading {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    user-select: none;
    font-size: 1.33em;
    
    & span {
      margin-top: 1em;
      color: greenyellow;
    }
  }

  .input > input {
    background: 0;
    border: 0;
    color: greenyellow;
    outline: none;
    width: 100%;
    height: 100%;

    padding: 0 .25ch;
  
    font-family: monospace;

    padding: .5em;

    border-top: 1px solid #fff3;
  }

  main {
    background: black;
    height: 100%;

    /* width: clamp(300px, 70%, 1200px); */

    display: flex;
    flex-direction: column;
    font-family: monospace;
  }

  .line {
    color: greenyellow;
    
    display: flex;
    flex-direction: column;

    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;

    margin-bottom: .5ch;
  }

  .line::selection {
    background-color: rgba(255, 255, 255, .25);
  }
</style>
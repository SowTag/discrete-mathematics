<script lang='ts'>
  import { onMount } from "svelte";

  import { loadPyodide } from 'pyodide'

  let lines: string[] = [];

  let currentEvent = 0;
  let ready = false;

  type KeyDownInputEvent = {
      target: HTMLInputElement,
      key: string  
  }

  function handleKeydown(event: KeyDownInputEvent) {
    
    if(event.key === 'Enter') {
      lines[currentEvent++] = event.target.value
      lines = lines
      event.target.value = ''
      console.log(lines)
    }
  }

  onMount(async() => {
    // Have pyodide cached
    const py = await loadPyodide();


    py.runPython()
  })
</script>


<main>
  
  {#each lines as line}
    <span class="line">{line}</span>
  {/each}


  <div class="input">
    <input on:keydown={handleKeydown} type="text" placeholder={ready ? "" : "Esperando al intérprete de Python..."}>
  </div>
</main>

<style>

  .input {
    margin-top: auto;
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

    width: clamp(300px, 70%, 1200px);

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
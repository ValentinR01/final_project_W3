<script lang=ts>
  export let primary = false;

  $: mode = primary ? 'button--primary' : 'button--secondary';
</script>

<button
  on:click
  class="{['button text-preset-4', mode].join(' ')}"
>            
    <slot/>
</button>


<style>
  .button{
    font-family: var(--font-family-primary);
    background-color: var(--color-primary);
    color: var(--color-text-light);
    border: var(--border-height-thick) solid var(--color-primary);
    border-radius: var(--small-radius);
    height: fit-content;
    padding: 10px 40px;
    cursor: pointer;
  }
  
  .button:hover{
    background-color: var(--color-secondary);
    border: var(--border-height-thick) solid var(--color-secondary);
  } 

  .button:active{
    background-color: var(--color-highlight);
    border: var(--border-height-thick) solid var(--color-highlight);
  }

  .button:disabled{  
    background-color: var(--color-disabled);
    border: var(--border-height-thick) solid var(--color-disabled);
  }

  .button:focus{ 
    border: var(--border-height-thick) solid var(--color-highlight);
  }
</style>
<script lang=ts>
  export let secondary = false;
  export let marginTop = "0";
</script>

<button
  on:click
  class="button text-preset-4 {secondary === true ? 'button--secondary' : ''} {$$props.class}"
  style='margin-top: {marginTop}'
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
    height: 30px;
    padding: 0 40px;
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

  .button--secondary{
    border: 1px solid var(--color-highlight);
    background-color: transparent;
    color: var(--color-highlight);
  }
</style>
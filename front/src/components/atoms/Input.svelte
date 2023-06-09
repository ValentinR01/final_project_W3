<script lang="ts">
  export let type = '';
  export let id = '';
  export let name = '';
  export let placeholder = '';
  export let width = '100%';
  export let value = '';

  function typeAction(node:any) {
      node.type = type;
  }
</script>

<input 
  use:typeAction
  id={id} 
  name={name} 
  placeholder={placeholder}
  class="input text-preset-5 {$$props.class}"
  style="width: {width}"
  bind:value
/>

<style>

  .input{
    color: var(--color-text-medium);
    border: var(--border-height-regular) solid var(--color-disabled);
    border-radius: var(--color-disabled);
    padding: var(--spacing-2);
    font-family: var(--font-family-primary);
    border-radius: var(--small-radius);
  }

  input::placeholder{
    font-size: var(--font-size-label-1);
    font-family: var(--font-family-primary);
  }

  .input:focus {
    color: var(--color-text-regular);
  }

  .input:focus-visible {
    outline: var(--border-height-regular) solid var(--color-highlight);
    outline-offset: -1px;
  }

  .input-valid {
      border: var(--border-height-thick) solid var(--color-highlight);
  }

  .input-invalid {
    border: var(--border-height-thick) solid #FF4D4D;
  }

  .input-with-icon{
    padding-right: 30px;
  }

</style>

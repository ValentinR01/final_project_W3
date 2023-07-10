<script lang="ts">
  export let type = '';
  export let id = '';
  export let name = '';
  export let placeholder = '';
  export let width = 'calc(100% - 20px)';
  export let value = '';

  /**
   * @type {boolean}
  */
  export let readonly = false;

  function typeAction(node:any) {
    node.type = type;
  }
</script>

{#if readonly}
  <input 
    use:typeAction
    id={id} 
    name={name} 
    class="input text-preset-5 {$$props.class}"
    style="width: {width}"
    value="{value}"
    readonly
  />
{:else}
  <input 
    use:typeAction
    id={id} 
    name={name} 
    placeholder={placeholder}
    class="input text-preset-5 {$$props.class}"
    style="width: {width}"
    bind:value
  />
{/if}

<style>

  .input{
    height: 18px;
    color: var(--color-text-medium);
    border: var(--border-height-regular) solid var(--color-disabled);
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
    height: 30px;
    padding-right: 20px;
  }

</style>

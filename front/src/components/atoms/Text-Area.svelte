<script>
  export let width = 'auto';
  export let placeholder = '';
  export let value = '';
</script>

<textarea 
  placeholder={placeholder}
  class="text-preset-5 {$$props.class}"
  style="width: {width}"
  bind:value
/>

<style>
  textarea {
    height: 75px;
    padding: var(--spacing-2);
    font-family: var(--font-family-primary);
    color: var(--color-text-medium);
    border: var(--border-height-regular) solid var(--color-disabled);
    border-radius: var(--small-radius);
  }

  textarea::placeholder{
    font-size: var(--font-size-label-1);
    font-family: var(--font-family-primary);
  }

  textarea:focus {
    color: var(--color-text-regular);
  }

  textarea:focus-visible {
    outline: var(--border-height-regular) solid var(--color-highlight);
    outline-offset: -1px;
  }
</style>
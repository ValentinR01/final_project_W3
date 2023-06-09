<script>
  /**
   * @type {string}
  */
  export let linkUrl = '#';
  export let linkColor = '';
</script>

<a href="{linkUrl}"
  on:click
  class="link {$$props.class}"
  style="color: {linkColor === 'grey' ? 'var(--color-text-medium)' : linkColor === 'blue' ? 'var(--color-primary)' : 'var(--color-text-regular)'}"
>          
    <slot/>
</a>

<style>
  .link{
    font-family: var(--font-family-primary);
    font-size: var(--font-size-regular);
    font-weight: var(--font-weight-light);
    text-decoration: none;
    display: inline-block;
  }
</style>
  
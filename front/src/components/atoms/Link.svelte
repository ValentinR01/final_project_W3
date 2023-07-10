<script>
  /**
   * @type {string}
  */
  export let linkUrl = '#';
  export let linkColor = '';
  export let linkStyle = '';
</script>

<a href="{linkUrl}"
  on:click
  class="link {$$props.class}"
  style="{linkStyle} color: {linkColor === 'grey' ? 'var(--color-text-dark)' : linkColor === 'blue' ? 'var(--color-primary)' : linkColor === 'white' ? 'var(--color-text-light:)' : 'var(--color-text-regular)'}"
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

  .link--current{
    color: var(--color-primary);
    text-decoration: underline;
    text-underline-offset: 5px;
  }

  .link--button{
    font-family: var(--font-family-primary);
    background-color: var(--color-primary);
    color: var(--color-text-light);
    border: var(--border-height-thick) solid var(--color-primary);
    border-radius: var(--small-radius);
    padding: 6px 40px;
    cursor: pointer;
  }
</style>
  
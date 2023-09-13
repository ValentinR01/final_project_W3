<script>
  /**
  * @type {Array<string>}
  */
  export let values;

  /**
   * @type {string | string[]}
  */
  export let disabled = [];
  
  /**
   * @type {string[]}
   */
   export let selectedOptions = [];

  /**
  * @type {any}
  */
  export let cat;
</script>
  
<div class='checkbox'>
  {#each values as option}
    {#if disabled.length > 0 && disabled.includes(option)}
      <input class="input-checkbox input-checkbox--disabled" type=checkbox id={option} value={option} name={cat} disabled>
      <label class="label-checkbox label-checkbox--disabled text-preset-5" for={option}> {option} </label>
    {:else}
      <input class="input-checkbox" type=checkbox id={option} value={option} name={cat} bind:group={selectedOptions}>
      <label class="label-checkbox text-preset-5" for={option}> {option} </label>
    {/if }
  {/each}
</div>

<style>
  .checkbox{
    display: flex;
    flex-wrap: wrap;
    row-gap: var(--spacing-2);
  }

  .label-checkbox{
    width: 150px;
    height: 15px;
  }

  .input-checkbox:checked,
  .input-checkbox:not(:checked) {
    position: absolute;
    left: -9999px;
  }

  .input-checkbox:checked + .label-checkbox,
  .input-checkbox:not(:checked) + .label-checkbox {
    position: relative;
    padding-left: var(--spacing-3);
    padding-right: var(--spacing-3);
    cursor: pointer;
  }

  .input-checkbox:checked + .label-checkbox:before,
  .input-checkbox:not(:checked) + .label-checkbox:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 13px;
    height: 13px;
    border: var(--border-height-regular) solid;
    border-color: var(--color-border);
    background: var(--white);
    -webkit-transition: border-color 0.3s ease;
    transition: border-color 0.3s ease;
  }

  .input-checkbox:checked + .label-checkbox:after,
  .input-checkbox:not(:checked) + .label-checkbox:after {
    content: '';
    width: 13px;
    height: 13px;
    background: var(--blue-base);
    position: absolute;
    top: 1px;
    left: 1px;
    -webkit-transition: all 0.1s ease;
    transition: all 0.1s ease;
  }

  .input-checkbox:not(:checked) + .label-checkbox:after {
    opacity: 0;
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  .input-checkbox:checked + .label-checkbox:after {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }

  .input-checkbox:checked + .label-checkbox:before{
    border-color: var(--blue-base);
  }

  .input-checkbox.input-checkbox--disabled + .label-checkbox:before{
    background: var(--color-disabled);
  }

  .label-checkbox.label-checkbox--disabled{
    color: var(--color-text-medium);
  }
</style>
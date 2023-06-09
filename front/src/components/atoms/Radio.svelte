<script>
  /**
  * @type {Array<string>}
  */
  export let values;

  /**
  * @type {String}
  */
  export let cat;
</script>

{#each values as option}
  <input class="input__radio" type=radio id={option} value={option} name={cat}>
  <label class="label__radio text-preset-5" for={option}> {option} </label>
{/each}

<style>
  .input__radio:checked,
  .input__radio:not(:checked) {
    position: absolute;
    left: -9999px;
  }

  .input__radio:checked + .label__radio,
  .input__radio:not(:checked) + .label__radio {
    position: relative;
    padding-left: var(--spacing-3);
    padding-right: var(--spacing-3);
    cursor: pointer;
  }

  .input__radio:checked + .label__radio:before,
  .input__radio:not(:checked) + .label__radio:before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    width: 13px;
    height: 13px;
    border: var(--border-height-regular) solid;
    border-color: var(--color-border);
    border-radius: 100%;
    background: var(--white);
  }

  .input__radio:checked + .label__radio:after,
  .input__radio:not(:checked) + .label__radio:after {
    content: '';
    width: 13px;
    height: 13px;
    background: var(--blue-base);
    position: absolute;
    top: 1px;
    left: 1px;
    border-radius: 100%;
    -webkit-transition: all 0.2s ease;
    transition: all 0.2s ease;
  }

  .input__radio:not(:checked) + .label__radio:after {
    opacity: 0;
    -webkit-transform: scale(0);
    transform: scale(0);
  }

  .input__radio:checked + .label__radio:after {
    opacity: 1;
    -webkit-transform: scale(1);
    transform: scale(1);
  }
</style>
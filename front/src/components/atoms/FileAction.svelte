<script>
  import Icon from "./Icon.svelte";
  import Exemple from "../../assets/img/video_thumbnail.png"

  /**
   * @type {any}
   */
   export let nameInput = 'file';
   export let action = 'upload';
   export let linkAction = '/projects/editor/add-metadata';

  /**
   * @type {any}
   */
  let files;

  let currentDate = new Date();

  /**
   * @param {Date} currentDate
   */
  function formatDate(currentDate) {
    const day = currentDate.getDate().toString().padStart(2, '0');
    const month = (currentDate.getMonth() + 1).toString().padStart(2, '0');
    const year = currentDate.getFullYear().toString();
    
    return `${day}/${month}/${year}`;
  }
</script>

<div class="file-action card">
  {#if action == 'download'}
    <a href="{Exemple}" download="saline_academy_{formatDate(currentDate)}">
      <div class="file-action__link">
        <Icon width=60 height=60>
          <slot name='icon' /> 
        </Icon>
        <span class="text-preset-3"> <slot name='text'/> </span>
      </div>
    </a>
  {:else if action == 'upload'}
    <label for={nameInput} class="file-action__link text-preset-3">
      <Icon width=60 height=60>
        <slot name='icon' /> 
      </Icon>
      <slot name='text'/>
    </label>
    <input id='{nameInput}' type="file" bind:files hidden>
  {:else}
    <a href="{linkAction}">
      <div class="file-action__link">
        <Icon width=60 height=60>
          <slot name='icon' /> 
        </Icon>
        <span class="text-preset-3"> <slot name='text'/> </span>
      </div>
    </a>
  {/if}
</div>

<style>
  .file-action__link{
    display: flex;
    column-gap: var(--spacing-3);
    justify-content: center;
    align-items: center;
  }

  .file-action a{
    text-decoration: none;
    color: var(--color-text-regular);
  }

</style>
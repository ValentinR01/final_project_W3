<script>
// @ts-nocheck
 
  import Link from "../../atoms/Link.svelte";
  import Icon from "../../atoms/Icon.svelte";
  import CloseIcon from "../../../assets/icons/CloseIcon.svelte";
  import Button from "../../atoms/Button.svelte";

  /**
   * @type {string}
  */
  export let id = 'modal-creation-project';

  let showModal = false;
  
  function toggleModal() {
    showModal = !showModal;
    document.body.classList.toggle('modal-open', showModal);
  }

</script>

<Button on:click={toggleModal}>Ouvrir modale</Button>

{#if showModal}
  <div id={id} class='modal-background {$$props.class}'>
    <div class='modal block-center'>
      <Link
        linkStyle="position: absolute; right: var(--spacing-4); top: var(--spacing-4);"
        on:click={toggleModal}
      >
        <Icon name="copy" width="10" height="10">
          <CloseIcon />
        </Icon> 
      </Link>
      <div class='modal__content block-center'>
        <slot />
      </div>
    </div>
  </div>
{/if}

<style>
  .modal-background{
    position: fixed;
    top: 0;
    width: 100%;
    height: 100vh;
    background: rgba(58, 79, 134, 0.1);
    backdrop-filter: blur(3.5px);
  }

  .modal{
    position: relative;
    top: 50%;
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    width: 600px;
    height: auto;
    padding: var(--spacing-5);
    background-color: var(--color-background-secondary);
    border-radius: var(--card-radius);
    overscroll-behavior: contain;
  }

</style>

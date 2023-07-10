<script>
  /**
   * @type {string}
  */
  export let imageSrc = '';
  export let imageAlt = 'image';
  export let imageWidth = 'auto';
  export let imageHeight = 'auto';

  /**
   * @type {boolean}
  */
  export let border = false;
</script>

<img
  src={imageSrc}
  alt={imageAlt}
  class='image {border === true ? 'image--border' : ''}'
  width={imageWidth}
  height={imageHeight}
/>

<style>
  .image{
    object-fit: cover;
  }

  .image--border{
    border-radius: var(--card-radius);
  }
</style>
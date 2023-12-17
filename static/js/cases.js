const toggleModal = (modalId, show = true) => {
    const modalEl = document.getElementById(modalId);
  
    if (show) {
      modalEl.classList.add("flex");
      modalEl.classList.remove("hidden");
      modalEl.setAttribute("aria-modal", "true");
      modalEl.setAttribute("role", "dialog");
      modalEl.removeAttribute("aria-hidden"); // create backdrop element
  
      var backdropEl = document.createElement("div");
      backdropEl.setAttribute("modal-backdrop", "");
      backdropEl.style.opacity = ".5";
      backdropEl.style.zIndex = "40";
      backdropEl.classList.add("bg-gray-900", "fixed", "inset-0");
      document.querySelector("body").append(backdropEl);
    } else {
      modalEl.classList.add("hidden");
      modalEl.classList.remove("flex");
      modalEl.setAttribute("aria-hidden", "true");
      modalEl.removeAttribute("aria-modal");
      modalEl.removeAttribute("role");
      document.querySelector("[modal-backdrop]").remove();
    }
  };
  
  window.toggleModal = toggleModal;
  document
    .querySelectorAll("[data-modal-toggle]")
    .forEach(function (modalToggleEl) {
      var modalId = modalToggleEl.getAttribute("data-modal-toggle");
      var modalEl = document.getElementById(modalId);
  
      if (
        !modalEl.hasAttribute("aria-hidden") &&
        !modalEl.hasAttribute("aria-modal")
      ) {
        modalEl.setAttribute("aria-hidden", "true");
      }
  
      modalToggleEl.addEventListener("click", function () {
        toggleModal(modalId, modalEl.hasAttribute("aria-hidden", "true"));
      });
    });
  